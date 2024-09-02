# core/data_manager.py

from utils.json_manager import load_json, save_json
from utils.xlsx_manager import load_xlsx, save_xlsx

def load_data(file_path):
    """Load data from a JSON or Excel file."""
    if file_path.endswith('.json'):
        return load_json(file_path)
    elif file_path.endswith('.xlsx'):
        return load_xlsx(file_path)
    else:
        raise ValueError("Unsupported file format")

def save_data(data, file_path):
    """Save data to a JSON or Excel file."""
    if file_path.endswith('.json'):
        save_json(data, file_path)
    elif file_path.endswith('.xlsx'):
        save_xlsx(data, file_path)
    else:
        raise ValueError("Unsupported file format")
