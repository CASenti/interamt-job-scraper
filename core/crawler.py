# core/crawler.py

import requests
from bs4 import BeautifulSoup
from utils.json_manager import save_json
from utils.xlsx_manager import save_xlsx

def start_crawl(urls):
    """Start the crawling process."""
    results = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Example: Extract all text from <p> tags
        paragraphs = soup.find_all('p')
        results.append({'url': url, 'content': [p.get_text() for p in paragraphs]})
    return results

def load_previous_results(json_file):
    """Load previously saved crawling results from a JSON file."""
    from utils.json_manager import load_json
    return load_json(json_file)

def save_results_as_json(data, json_file):
    """Save crawling results as JSON on the run."""
    save_json(data, json_file)

def save_final_results_as_xlsx(data, xlsx_file):
    """Save final crawling results into an Excel file."""
    save_xlsx(data, xlsx_file)

def set_crawl_targets(tags):
    """Set what to crawl for, e.g., specific HTML tags or classes."""
    return tags  # Example: returning tags or CSS selectors for further processing
