# Interamt Job Scraper for German Public Sector

**Project Description:**

This Python project is designed to automate the process of gathering and filtering job listings from the German public sector job portal, [Interamt.de](https://interamt.de), also known as "Das Karriereportal des öffentlichen Dienstes." The portal hosts job offers from various partner institutions across Germany, particularly for positions in the public sector.

**Technical Description:**

The project comprises a two-stage process: an initial URL crawling to gather a base list of job listings and a subsequent data scraping process to filter and extract detailed job information based on specific criteria.

---

### Project Structure

The project is modular, allowing for a clear separation of responsibilities, such as crawling, filtering, and scraping. Below is a brief overview of the main components:

```plaintext
interamt-job-scraper/
│
├── core/
│   ├── __init__.py
│   ├── crawler.py
│   ├── data_manager.py
│   └── config.py
│
├── filter/
│   ├── __init__.py
│   └── filter_processor.py
│
├── scraper/
│   ├── __init__.py
│   ├── scraper.py
│   ├── data_manager.py
│   └── config.py
│
├── utils/
│   ├── __init__.py
│   ├── file_manager.py
│   ├── json_manager.py
│   └── xlsx_manager.py
│
├── main.py
└── requirements.txt
```

The project is organized into several modules:

- **Core Module (`core/`)**: 
  - Handles the initial crawling of URLs to create a base list for each partner institution on Interamt by iterating through all partner IDs
  - Manages data loading and saving operations
  
- **Filter Module (`filter/`)**:
  - Filters the base list based on specific criteria (a predefined list), particularly focusing on the "Oberste Bundesbehörden" (Supreme Federal Authorities of Germany)
   
- **Scraper Module (`scraper/`)**:
  - Extracts all job listings from the filtered list of partner institutions
  - Saves the extracted data in JSON and Excel formats for easy access and further analysis

- **Utilities (`utils/`)**:
  - Provides general-purpose functions for file handling, JSON processing, and Excel management

---

### Features

- **Modular Design**: Each functionality is encapsulated within its own module, making the code easy to maintain and extend.
- **Dynamic URL Crawling**: Automatically generates URLs for each partner institution based on their unique IDs.
- **Targeted Filtering**: Focuses on key federal authorities to ensure that the most relevant job listings are retrieved.
- **Comprehensive Data Handling**: Supports both JSON and Excel formats for storing the scraped data, making it accessible for various use cases.

---

### How It Works

1. **URL Crawling**: 
   - The project starts by crawling through all URLs of Interamt's partner institutions. Each partner institution has a unique ID appended to the base URL (`https://interamt.de/koop/app/trefferliste?partner=`), which is dynamically generated and crawled using BeautifulSoup (bs4). 
   - For instance, the Bundesministerium für Bildung und Forschung (Federal Ministry of Education and Research) has the partner ID "240", so its URL would be `https://interamt.de/koop/app/trefferliste?partner=240`.
   - This crawling process generates a base list of URLs corresponding to each partner institution's job page.

2. **Filtering**:
   - The project includes a filter mechanism based on a predefined list of all 31 "Oberste Bundesbehörden" (Supreme Federal Authorities of Germany). The filter is applied to the base list of URLs to isolate those belonging to these key federal institutions.
   - The list of these authorities is sourced from [Wikipedia](https://de.wikipedia.org/wiki/Bundesbeh%C3%B6rde_(Deutschland)#Oberste_Bundesbeh%C3%B6rden).

3. **Data Scraping**:
   - Once the filtering is applied, the scraper is triggered to extract job listings from the filtered URLs.
   - The extracted data is saved as JSON files during the scraping process and is also compiled into an Excel file upon completion.

---

### Example Workflow

- **Crawl**: The script crawls all partner URLs by appending partner IDs to the base URL, generating a comprehensive list of job pages across the public sector.
- **Filter**: The list is filtered to focus on the 31 Supreme Federal Authorities, ensuring that only job listings from these key institutions are processed.
- **Scrape**: The scraper then extracts relevant job listings from the filtered list, storing them for further analysis or reporting.

---

### Installation and Usage

To get started with this project:

1. **Clone the Repository**

    ```bash
   git clone https://github.com/yourusername/interamt-job-scraper.git
   cd interamt-job-scraper
   ```

2. **Install Dependencies**

   Ensure you have Python installed. Then install the required packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. **Update Configuration**

   Modify the `config.py` file in the `core` directory to set any required configuration options such as base URLs
   
4. **Run the Script**

   **Crawl:** You can run the main script to start the crawling, filtering, and scraping process:

   ```bash
   python main.py --action crawl
   ```

   This will generate a JSON file containing the initial base list of URLs.


   **Filter:** To filter job postings based on specific federal authorities, update the filter criteria file (`filter_criteria.json`) and then run:

   ```bash
   python main.py --action filter
   ```

   This will create a filtered list of URLs based on the provided criteria.

   **Scrape:** With the filtered data, you can run the data scraper to extract detailed job postings:

   ```bash
   python main.py --action scrape
   ```

   The scraper will save the results in both JSON and XLSX formats.

---

### Contribution

Contributions are welcome! Please fork the repository and submit a pull request with your improvements or bug fixes. Feel free to contribute to the project by submitting issues or pull requests. If you have suggestions for improvements or need help, please open an issue on the [GitHub repository](https://github.com/yourusername/job-data-scraper/issues).

---

### License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0) - see the [LICENSE](LICENSE) file for details.
