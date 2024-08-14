from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv

# Set up the Selenium WebDriver (e.g., Chrome)
service = Service('C:\\WebDriver\\chromedriver.exe') 
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = 'https://journals.sagepub.com/toc/JMX/current'
driver.get(url)

page_content = driver.page_source
soup = BeautifulSoup(page_content, 'html.parser')

# Find the main container div with class 'table-of-content'
content_div = soup.find("div", class_="table-of-content")

# Find all sections within the main container
sections = content_div.find_all("section")

# Prepare to write to a CSV file
with open('articles.csv', mode='w', newline='', encoding='utf-8-sig') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write the header row
    csv_writer.writerow(['Title', 'Authors', 'First Published Date', 'DOI', 'Abstract'])

    # Iterate over each section and extract the required information
    for section in sections:
        # 1. Extract the title
        title_tag = section.find("h5", class_="issue-item__heading")
        title = title_tag.get_text(strip=True) if title_tag else "No title available"

        # 2. Extract author names (affiliations are not provided in the given HTML)
        authors = []
        author_tags = section.find_all("span", id=lambda x: x and x.startswith("author"))
        for author in author_tags:
            authors.append(author.get_text(strip=True))
        authors_text = ", ".join(authors) if authors else "No authors listed"

        # 3. Extract first published date
        published_date_tag = section.find("div", class_="issue-item__header")
        published_date_full = published_date_tag.find_all("span")[-2].get_text(strip=True) if published_date_tag else "No date available"
        published_date = published_date_full.replace("First published", "").strip()

        # 4. Extract DOI
        doi_tag = section.find("a", {"data-id": "toc-article-title"})
        doi = doi_tag['href'].split('/')[-1] if doi_tag else "No DOI available"
        doi = f"'{doi}"  # Prefix with a single quote to ensure Excel treats it as text


        # 5. Extract abstract
        abstract_section = section.find("div", class_="issue-item__abstract__content")
        if abstract_section:
            abstract_text = abstract_section.get_text(strip=True)
            abstract = abstract_text.replace("Abstract", "", 1).strip()
        else:
            abstract = "No abstract available"

        csv_writer.writerow([title, authors_text, published_date, doi, abstract])

        # Print extracted information
        print(f"Title: {title}")
        print(f"Authors: {authors_text}")
        print(f"First Published Date: {published_date}")
        print(f"DOI: {doi}")
        print(f"Abstract: {abstract}")
        print("-" * 40)  # Separator for clarity between articles


# Close the browser
driver.quit()

print("Data has been written to articles.csv")

