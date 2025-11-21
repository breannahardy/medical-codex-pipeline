import sys
import os

# Force Python to include the project root (this folder)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

import pandas as pd
import logging
from utils.common_functions import save_to_formats

RAW_FILE = "input/hcpcs_codes_2024.txt"

def main():
    logging.basicConfig(level=logging.INFO)

    df = pd.read_csv(
        RAW_FILE,
        sep="|",
        header=None,
        names=["code", "description", "status"],
        dtype=str,
        engine="python"
    )

    # Clean fields
    df["code"] = df["code"].str.strip().str.upper()
    df["description"] = df["description"].str.strip()

    # Keep only code + description (assignment requirement)
    df = df[["code", "description"]]

    save_to_formats(df, "output/csv/hcpcs_2024")

    logging.info("HCPCS processing complete.")


if __name__ == "__main__":
    main()
