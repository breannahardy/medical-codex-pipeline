import pandas as pd
import logging
from pathlib import Path
from datetime import datetime

def save_to_formats(df: pd.DataFrame, base_filename: str):
    """
    Save DataFrame to consistent output formats.
    Saves: CSV only (assignment requirement)
    """
    output_path = Path(base_filename)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Add timestamp column
    df["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    csv_path = f"{base_filename}.csv"
    df.to_csv(csv_path, index=False)
    logging.info(f"Saved CSV → {csv_path}")

