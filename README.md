# Medical Codex Pipeline - Assignment1 
The purpose of this assignment is to develop a data pipeline that processes multiple medical codexes into standardized, clean, and validated formats. It aims to provide hands-on experience with healthcare data, including data loading, validation, cleaning, and data output.

## Medical Codexes
The medical codexes files that were used are:
1. **SNOMED CT (US)** - https://www.nlm.nih.gov/healthit/snomedct/index.html
2. **ICD-10-CM (US)** - https://www.cms.gov/medicare/coding-billing/icd-10-codes
3. **ICD-10 (WHO)** - https://icdcdn.who.int/icd10/index.html
4. **HCPCS (US)** - https://www.cms.gov/medicare/coding-billing/hcpcscode
5. **LOINC (US)** -  https://loinc.org/downloads/
6. **RxNorm (US)** - https://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html
7. **NPI (US)** - https://download.cms.gov/nppes/NPI_Files.html

## Setup 
1. Create python virtual environment - .venv file
2. Activate environment 
3. Install all required packages 
4. For each medical codex, a Python script was created to:
- Load the input file
- Validate code formats
- Standardize text fields amd clean data
- Handle missing or null values
Output files include standardized columns:
- code – the primary identifier
- description – human-readable description
- last_updated – processing timestamp
A shared utilities module contains reusable functions, including:
- save_to_formats(df, base_filename) – saves a DataFrame to CSV across all scripts

## Respository Structure
medical-codex-pipeline/
├── input/                  # Raw data files (excluded from GitHub, specified in .gitignore)
├── scripts/                # Processing scripts for each codex
│   ├── snomed_processor.py
│   ├── icd10cm_processor.py
│   ├── icd10who_processor.py
│   ├── hcpcs_processor.py
│   ├── loinc_processor.py
│   ├── rxnorm_processor.py
│   └── npi_processor.py
├── output/                 # Processed outputs (CSV)
│   └── csv/
├── utils/                  # Common utilities
│   └── common_functions.py
├── requirements.txt
└── README.md
