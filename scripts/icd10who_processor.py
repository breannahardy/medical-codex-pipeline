import sys
import os
import pandas as pd
import logging

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from utils.common_functions import save_to_formats

# Uploaded WHO ICD-10 files
CODES_FILE = "input/icd102019syst_codes.txt"
GROUPS_FILE = "input/icd102019syst_groups.txt"

def load_icd10who():
    """
    Load WHO ICD-10 system files.
    codes file format:
        CODE<TAB>DESCRIPTION
    groups file format (optional):
        CATEGORY<TAB>DESCRIPTION
    """

    # Load the main codes file (the one with all ICD-10 codes)
    df_codes = pd.read_csv(
        CODES_FILE,
        sep="\t",
        header=None,
        names=["code", "description"],
        dtype=str,
        engine="python"
    )

    # Some lines may be empty or malformed
    df_codes = df_codes.dropna(subset=["code"])

    # Clean whitespace
    df_codes["code"] = df_codes["code"].str.strip().str.upper()
    df_codes["description"] = df_codes["description"].str.strip()

    return df_codes


def main():
    logging.basicConfig(level=logging.INFO)

    logging.info("Loading WHO ICD-10 (2019) codes...")
    df = load_icd10who()

    logging.info(f"Loaded {len(df)} ICD-10-WHO rows.")

    # Save CSV
    save_to_formats(df, "output/csv/icd10who")

    logging.info("ICD-10-WHO processing complete!")


if __name__ == "__main__":
    main()
