# main.py

from core.crawler import start_crawl, save_final_results_as_xlsx, set_crawl_targets
from filter.filter_processor import load_filter_list, apply_filter
from scraper.scraper import start_scrape, save_final_results_as_xlsx as save_scrape_results

def main():
    # Step 1: Start crawling process
    urls = ["https://example.com", "https://another-example.com"]  # Example URLs
    set_crawl_targets(['p', 'h1'])  # Set tags to crawl for
    crawl_results = start_crawl(urls)
    
    # Step 2: Save intermediate crawl results
    save_final_results_as_xlsx(crawl_results, 'crawl_results.xlsx')
    
    # Step 3: Load and apply filters
    filter_list = load_filter_list('filters.txt')  # Load filter list from a file
    filtered_data = apply_filter(crawl_results, filter_list)
    
    # Step 4: Start scraping process on filtered data
    scrape_results = start_scrape(filtered_data)
    
    # Step 5: Save final scrape results
    save_scrape_results(scrape_results, 'scrape_results.xlsx')

if __name__ == "__main__":
    main()
