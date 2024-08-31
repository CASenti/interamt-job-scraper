# Job Data Scraper for Public Sector

## Overview

This project is designed to collect and analyze job postings from the German public sector job search site [Interamt](https://interamt.de), known as "Das Karriereportal des öffentlichen Dienstes." The project comprises a two-stage process: an initial URL crawling to gather a base list of job listings and a subsequent data scraping process to filter and extract detailed job information based on specific criteria.

### Project Structure

```
interamt-job-scraper/
│
├── core/
│   ├── __init__.py
│   ├── url_crawler.py
│   ├── data_handler.py
│   └── config.py
│
├── filter/
│   ├── __init__.py
│   ├── filter_processor.py
│
├── scraper/
│   ├── __init__.py
│   ├── data_scraper.py
│   └── result_saver.py
│
├── utils/
│   ├── __init__.py
│   ├── json_utils.py
│   └── xlsx_utils.py
│
├── main.py
└── requirements.txt
```

The project is organized into several modules:
- **`core/url_crawler.py`**: Handles the initial crawling of URLs from partner institutions on Interamt. It creates a base list of job listings by iterating through all partner IDs.
- **`filter/filter_processor.py`**: Applies filters to the base list based on a predefined list of "Oberste Bundesbehörden" (highest federal authorities) to refine the data.
- **`scraper/data_scraper.py`**: Scrapes detailed job postings from the filtered data, extracting relevant information from specific partner pages.
- **`scraper/result_saver.py`**: Saves the scraped results in JSON and XLSX formats.
- **`utils/json_utils.py`** and **`utils/xlsx_utils.py`**: Provide utility functions for handling JSON and XLSX files.

---

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/job-data-scraper.git
   cd job-data-scraper
   ```

2. **Install Dependencies**

   Make sure you have Python installed, then install the required packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. **Update Configuration**

   Modify the `config.py` file in the `core` directory to set any required configuration options such as base URLs or API keys.

---

### Usage

1. **Run the URL Crawler**

   The URL crawler collects a base list of job postings from Interamt for all partner institutions.

   ```bash
   python main.py --action crawl
   ```

   This will generate a JSON file containing the initial base list of URLs.

2. **Apply Filters**

   To filter job postings based on specific federal authorities, update the filter criteria file (`filter_criteria.json`) and then run:

   ```bash
   python main.py --action filter
   ```

   This will create a filtered list of URLs based on the provided criteria.

3. **Run the Data Scraper**

   With the filtered data, you can run the data scraper to extract detailed job postings:

   ```bash
   python main.py --action scrape
   ```

   The scraper will save the results in both JSON and XLSX formats.

---

### Example

- **Initial Crawl**: 

  The URL crawler will generate URLs like:
  ```plaintext
  https://interamt.de/koop/app/trefferliste?partner=240
  ```

- **Filtering**:

  Using the list of "Oberste Bundesbehörden" from [Wikipedia](https://de.wikipedia.org/wiki/Bundesbeh%C3%B6rde_(Deutschland)#Oberste_Bundesbeh%C3%B6rden), filter to find job postings from specific federal authorities.

- **Data Scraping**:

  For each filtered URL, the scraper extracts job postings and saves them in a structured format.

---

### Files

- **`config.py`**: Configuration settings.
- **`filter_criteria.json`**: JSON file containing filter criteria.
- **`base_results.json`**: Output from the URL crawler.
- **`scraped_results.json`**: Output from the data scraper.
- **`scraped_results.xlsx`**: Excel file containing scraped job postings.

---

### Contribution

Feel free to contribute to the project by submitting issues or pull requests. If you have suggestions for improvements or need help, please open an issue on the [GitHub repository](https://github.com/yourusername/job-data-scraper/issues).

---

### License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0) - see the [LICENSE](LICENSE) file for details.
