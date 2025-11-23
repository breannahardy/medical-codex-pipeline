import sys
import os

# Add project root to system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import polars as pl
from polars import selectors as cs
from datetime import datetime
from utils.common_functions import save_to_formats

# Define the file path
file_path = r"C:\Users\hardy\Documents\HHA 507\medical-codex-pipeline\medical-codex-pipeline-1\input\npi_data.csv"

# Load the first 1000 rows
df = pl.read_csv(file_path, n_rows=1000)

# Print columns to verify names
print("Columns:", df.columns)

# Select columns (case-insensitive pattern)
df_small = df.select([
    pl.col('NPI').alias('code'),
    pl.col('Provider Last Name (Legal Name)').alias('description')
])

# Add timestamp
df_small = df_small.with_columns([
    pl.lit(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).alias('last_updated')
])

# Remove empty descriptions
df_small = df_small.filter(
    (pl.col('description').is_not_null()) & 
    (pl.col('description').str.strip_chars() != "")
)

# Save output
output_base = 'output/npi_data'
save_to_formats(df_small, output_base)

print(f"Successfully parsed {df_small.height} records from {file_path}")
print(f"Saved to {output_base}.csv")
print(df_small.head())
