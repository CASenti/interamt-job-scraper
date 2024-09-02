# utils/file_manager.py

import os

def load_file(file_path):
    """Load a file based on its type."""
    with open(file_path, 'r') as file:
        return file.read()

def save_file(data, file_path):
    """Save data to a file."""
    with open(file_path, 'w') as file:
        file.write(data)
