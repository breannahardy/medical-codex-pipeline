import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

import pandas as pd
import logging
import re
from utils.common_functions import save_to_formats

RAW_FILE = "input/icd10cm_codes_2024.txt"

def load_icd10cm(filepath):
    """Load ICD-10-CM where code + description are in one column."""
    df = pd.read_csv(filepath, header=None, names=["raw"], dtype=str)

    # Extract ICD code using regex
    df["code"] = df["raw"].str.extract(r'([A-TV-Z][0-9]{2}(?:\.[0-9A-Z]{1,4})?)')

    # Description = everything after the code
    df["description"] = df["raw"].str.replace(
        r'^[A-TV-Z][0-9]{2}(?:\.[0-9A-Z]{1,4})?\s*', '', regex=True
    )

    df = df[["code", "description"]]
    return df

def clean_icd10cm(df):
    df["code"] = df["code"].str.strip().str.upper()
    df["description"] = df["description"].str.strip()
    return df

def main():
    logging.basicConfig(level=logging.INFO)

    raw_df = load_icd10cm(RAW_FILE)
    clean_df = clean_icd10cm(raw_df)

    save_to_formats(clean_df, "output/csv/icd10cm_2024")

    logging.info("ICD-10-CM processing completed.")

if __name__ == "__main__":
    main()
