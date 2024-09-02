# filter/filter_processor.py

def load_filter_list(filter_file):
    """Load the list used for filtering."""
    with open(filter_file, 'r') as f:
        filters = f.read().splitlines()
    return filters

def apply_filter(data, filter_list):
    """Apply the filter to the base data."""
    filtered_results = []
    for entry in data:
        filtered_content = [text for text in entry['content'] if any(f in text for f in filter_list)]
        if filtered_content:
            filtered_results.append({'url': entry['url'], 'content': filtered_content})
    return filtered_results
