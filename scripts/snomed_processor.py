import sys
import os

# Add project root to system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import polars as pl
from datetime import datetime
import os

def save_to_formats(df: pl.DataFrame, output_base: str):
    os.makedirs(os.path.dirname(output_base), exist_ok=True)
    df.write_csv(output_base + ".csv")
    df.write_parquet(output_base + ".parquet")
    print(f"Saved: {output_base}.csv & .parquet")


# -----------------------
# SNOMED CT PROCESSOR
# -----------------------
SNOMED_DESC = r"C:\PATH\TO\sct2_Description_Snapshot-en.txt"   # <-- UPDATE THIS
SNOMED_CONCEPT = r"C:\PATH\TO\sct2_Concept_Snapshot.txt"       # <-- UPDATE THIS


def process_snomed():
    print("Loading SNOMED CT...")

    desc_df = pl.read_csv(SNOMED_DESC, sep="\t")
    concept_df = pl.read_csv(SNOMED_CONCEPT, sep="\t")

    # Join on conceptId and keep only active concepts
    snomed_df = desc_df.join(
        concept_df.select([pl.col("id").alias("conceptId"), pl.col("active")]),
        on="conceptId",
        how="inner"
    ).filter(pl.col("active") == 1)

    snomed_small = snomed_df.select([
        pl.col("conceptId").alias("code"),
        pl.col("term").alias("description")
    ]).with_columns([
        pl.lit(datetime.now().strftime("%Y-%m-%d %H:%M:%S")).alias("last_updated")
    ])

    save_to_formats(snomed_small, "output/snomed_data")
    print(f"SNOMED CT parsed {snomed_small.height} rows.")


if __name__ == "__main__":
    process_snomed()
