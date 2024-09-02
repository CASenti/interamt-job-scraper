# utils/xlsx_manager.py

import pandas as pd

def load_xlsx(xlsx_file):
    """Load data from an Excel file."""
    return pd.read_excel(xlsx_file).to_dict(orient='records')

def save_xlsx(data, xlsx_file):
    """Save data to an Excel file."""
    df = pd.DataFrame(data)
    df.to_excel(xlsx_file, index=False)

def update_xlsx(existing_xlsx_file, new_data):
    """Update an existing Excel file with new data."""
    df_existing = pd.read_excel(existing_xlsx_file)
    df_new = pd.DataFrame(new_data)
    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    df_combined.to_excel(existing_xlsx_file, index=False)
