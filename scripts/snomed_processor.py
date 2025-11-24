import sys
from pathlib import Path

# Add the project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))
import polars as pl
from datetime import datetime
from utils.common_functions import save_to_formats

# Define the file path
file_path = r'C:\Users\hardy\Documents\HHA 507\medical-codex-pipeline\input\sct2_Description_Full-en_US1000124_20250901.txt'
# Read the SNOMED CT file as a polars DataFrame
df = pl.read_csv(
    file_path,
    separator='\t',
    has_header=True,
    quote_char=None,
    encoding='utf8-lossy',
    truncate_ragged_lines=True,
    dtypes={
        'id': pl.Utf8,
        'effectiveTime': pl.Utf8,
        'active': pl.Int32,
        'moduleId': pl.Utf8,
        'conceptId': pl.Utf8,
        'languageCode': pl.Utf8,
        'typeId': pl.Utf8,
        'term': pl.Utf8,
        'caseSignificanceId': pl.Utf8
    }
)

# Print unique language codes present in the DataFrame
print(f"\nActive terms count: {df.filter(pl.col('active') == 1).height}")
lang_series = df.get_column('languageCode')
print(f"Language codes: {lang_series.unique().to_list()}")

# Save only a sample of the first 1,000 rows to reduce file size
df_sample = df.head(1000)

# Add a last_updated column with the current timestamp
df_sample = df_sample.with_columns([
    pl.lit(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).alias('last_updated')
])

# Save the sampled DataFrame to CSV using the reusable function
output_base = 'output/snomed_descriptions_sample'
save_to_formats(df_sample, output_base)


# Print summary and preview for the sampled DataFrame
print(f"Successfully parsed {df_sample.height} records from SNOMED CT file")
print(f"Saved to {output_base}.csv")
print(f"Dataset shape: {df_sample.shape}")
print(f"\nColumn names: {df_sample.columns}")
print(f"\nFirst 5 rows:")
print(df_sample.head())