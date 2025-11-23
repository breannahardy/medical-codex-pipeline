import polars as pl
import pandas as pd
from pathlib import Path

def save_to_formats(df, base_filename):
    # Save a DataFrame (pandas or polars) to CSV format.
    csv_path = Path(f"{base_filename}.csv")
    if isinstance(df, pd.DataFrame):
        df.to_csv(csv_path, index=False)
        print(f"pandas DataFrame saved to {csv_path}")
    elif isinstance(df, pl.DataFrame):
        df.write_csv(csv_path)
        print(f"polars DataFrame saved to {csv_path}")
    else:
        raise TypeError("df must be a pandas.DataFrame or polars.DataFrame")