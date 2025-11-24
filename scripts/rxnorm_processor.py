import sys
from pathlib import Path
from datetime import datetime
import polars as pl

# Add project root to sys.path so utils can be found
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

# Import reusable function
from utils.common_functions import save_to_formats

# Define file path
file_path = r"C:\Users\hardy\Documents\HHA 507\medical-codex-pipeline\input\RXNATOMARCHIVE.RRF"

# Column names for RXNATOMARCHIVE.RRF
columns = [
    'rxaui', 'aui', 'str', 'archive_timestamp', 'created_timestamp',
    'updated_timestamp', 'code', 'is_brand', 'lat', 'last_released',
    'saui', 'vsab', 'rxcui', 'sab', 'tty', 'merged_to_rxcui'
]

# Read RXNATOMARCHIVE.RRF 
df = pl.read_csv(
    file_path,
    separator='|',        
    has_header=False,     
    new_columns=columns,  
    ignore_errors=True   
)

# Keep only relevant columns
df_small = df.select([
    pl.col('code'),               
    pl.col('str').alias('description')  
])

# Add last_updated timestamp
last_updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
df_small = df_small.with_columns([pl.lit(last_updated).alias('last_updated')])

# Prepare output path
output_dir = Path('output')
output_dir.mkdir(exist_ok=True)
output_base = output_dir / 'rxnorm_codes'

# Save full dataset
save_to_formats(df_small, output_base)

# Save small sample (first 1000 rows)
sample_output_base = output_dir / 'rxnorm_codes'
save_to_formats(df_small.head(1000), sample_output_base)

# Summary information
print(f"Successfully parsed {df_small.height} records from RXNATOMARCHIVE.RRF")
print(f"Saved full dataset to {output_base}.csv and {output_base}.parquet")
print(f"Saved sample dataset to {sample_output_base}.csv and {sample_output_base}.parquet")
print(f"Dataset shape: {df_small.shape}")

# Safe print of first 5 rows
try:
    print("\nFirst 5 rows:")
    print(df_small.head())
except UnicodeEncodeError:
    print("\nFirst 5 rows (ASCII-safe):")
    print(df_small.head().to_pandas().applymap(lambda x: str(x).encode('ascii', errors='replace').decode()))
