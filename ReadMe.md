
# SAGE Journals Data Extractor

## Overview

This project provides a Python script to extract article details from the SAGE Journals website and save the data into a CSV file. The extracted data includes the article's title, authors, publication date, DOI, and abstract.

## Prerequisites

Before running the script, ensure you have the following installed:

1. **Python**: You can download Python from [python.org](https://www.python.org/downloads/).
2. **pip**: Package installer for Python, typically included with Python installations.

## Installation

To set up the project, follow these steps:

1. Clone the repository to your local machine.
   
   ```bash
   git clone <your-repository-url>
   ```

2. Navigate to the project directory.

   ```bash
   cd <your-project-directory>
   ```

3. Install the required Python packages using `pip`.

   ```bash
   pip install selenium bs4
   ```
- Note: As the website is protected by cloudflare anti-bot system, which is presenting a challenge to verify that the request is being made by a human. we use selenium to automate the chrome actions.

4. Download and install the Chrome WebDriver:
   - Visit the [ChromeDriver download page](https://googlechromelabs.github.io/chrome-for-testing/#stable).
   - Download the version that matches your installed version of Chrome.
   - Extract the `chromedriver.exe` file and note its location.

## Usage

To run the script and extract data:

1. Open the `scrape_sage.py` script and update the WebDriver path:

   ```python
   service = Service('C:\\Path\\To\\Your\\chromedriver.exe')
   ```

2. Run the script:

   ```bash
   python scrape_sage.py
   ```

3. The script will fetch the data from the SAGE Journals website and save it into a `articles.csv` file in the project directory.


### CSV Output

- The CSV file will include columns for `Title`, `Authors`, `First Published Date`, `DOI`, and `Abstract`.
- The DOI is formatted as text to avoid issues with Excel interpreting it as a number.

## Troubleshooting

- **Character Encoding**: The CSV file is encoded in `utf-8-sig` to ensure special characters display correctly.
- **DOI Formatting**: DOIs are prefixed with a single quote to prevent them from being converted to scientific notation in Excel.

## Conclusion

This script automates the process of extracting article data from SAGE Journals and storing it in a CSV file, making it easier to analyze or share the information.