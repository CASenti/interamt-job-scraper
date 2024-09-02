# scraper/settings.py

class ScrapeSettings:
    HEADERS = {
        'User-Agent': 'Mozilla/5.0'
    }
    TARGET_TAGS = ['a', 'img']  # Example tags to scrape for additional information
