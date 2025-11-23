import polars as pl
from pathlib import Path
from datetime import datetime
from utils.common_functions import save_to_formats


# Define the file path
file_path = r"C:\Users\hardy\Documents\HHA 507\medical-codex-pipeline\medical-codex-pipeline\input\RXNATOMARCHIVE.RRF"

#List of column names for RXNATOMARCHIVE.RRF
columns = [
    'rxaui', 'aui', 'str', 'archive_timestamp', 'created_timestamp',
    'updated_timestamp', 'code', 'is_brand', 'lat', 'last_released',
    'saui', 'vsab', 'rxcui', 'sab', 'tty', 'merged_to_rxcui'
]


# Read the RXNATOMARCHIVE.RRF file as a polars DataFrame
df = pl.read_csv(
    file_path,
    sep='|',
    has_header=False,
    new_columns=columns,
    truncate_ragged_lines=True
)


# Add a last_updated column with the current timestamp
last_updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
df = df.with_columns([pl.lit(last_updated).alias('last_updated')])


# Prepare output directory and path
output_dir = Path('output')
output_dir.mkdir(exist_ok=True)
output_base = output_dir / 'rxnorm_codes'

# Save the DataFrame to CSV using the reusable function
save_to_formats(df, output_base)

# Print summary information
print(f"Successfully parsed {df.height} records from RXNATOMARCHIVE.RRF")
print(f"Saved to {output_base}.csv")
print(f"Dataset shape: {df.shape}")
print("\nFirst 5 rows:")
print(df.head())