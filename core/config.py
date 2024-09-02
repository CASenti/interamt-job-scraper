# core/settings.py

class CrawlSettings:
    BASE_URLS = [
        "https://example.com",
        "https://another-example.com"
    ]
    HEADERS = {
        'User-Agent': 'Mozilla/5.0'
    }
    TARGET_TAGS = ['p', 'h1', 'h2']  # Example tags to crawl for
