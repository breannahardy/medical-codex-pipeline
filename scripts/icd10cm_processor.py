import pandas as pd
import logging
from pathlib import Path
from utils.common_functions import validate_code_format, save_to_formats

logger = logging.getLogger(__name__)

def load_icd10cm_data(filepath):
    """Load raw ICD-10-CM data file"""
    logger.info(f"Loading ICD-10-CM data from {filepath}")
    df=pd.read_csv(filepath, sep=r"\s{2}",names= ["icd_code", "description"],engine='python', header=None)
    logger.info(f"Loaded {len(df)} records")
    return df

def clean_icd10cm_data(raw_data):
    """Clean and standardize ICD-10-CM codes"""
    logger.info(raw_data)
    return raw_data

def main():
    logging.basicConfig(level=logging.INFO)
    # Load raw data
    raw_data = load_icd10cm_data("input/icd10cm_codes_2024.txt")
    # Clean and process
    clean_data = clean_icd10cm_data(raw_data)
    # Save outputs
    save_to_formats(clean_data, "output/icd10cm_2024")
    logging.info("ICD-10-CM processing completed")

if __name__ == "__main__":
    main()
