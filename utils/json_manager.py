# utils/json_manager.py

import json

def load_json(json_file):
    """Load data from a JSON file."""
    with open(json_file, 'r') as file:
        return json.load(file)

def save_json(data, json_file):
    """Save data to a JSON file."""
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)
