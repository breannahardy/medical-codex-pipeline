import sys
import os
import pandas as pd
import logging

# add project root to python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from utils.common_functions import save_to_formats

# Path to your LOINC input file
LOINC_FILE = "input/loinc_sample.csv"

def load_loinc(filepath):
    """
    Load LOINC file.
    Expected important fields:
        - LOINC_NUM
        - LONG_COMMON_NAME
    """
    df = pd.read_csv(filepath, dtype=str)

    # Ensure required columns exist
    if "LOINC_NUM" not in df.columns or "LONG_COMMON_NAME" not in df.columns:
        raise ValueError(
            "Missing required LOINC columns. Expected: LOINC_NUM and LONG_COMMON_NAME"
        )

    return df[["LOINC_NUM", "LONG_COMMON_NAME"]]


def clean_loinc(df):
    """Clean and standardize LOINC codes."""
    df["code"] = df["LOINC_NUM"].str.strip()
    df["description"] = df["LONG_COMMON_NAME"].str.strip()

    df = df[["code", "description"]]
    return df


def main():
    logging.basicConfig(level=logging.INFO)

    logging.info("Loading LOINC data...")
    raw_df = load_loinc(LOINC_FILE)

    logging.info("Cleaning LOINC data...")
    clean_df = clean_loinc(raw_df)

    save_to_formats(clean_df, "output/csv/loinc")

    logging.info("LOINC processing complete.")


if __name__ == "__main__":
    main()
