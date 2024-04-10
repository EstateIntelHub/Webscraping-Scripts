import re
import csv
import glob
from bs4 import BeautifulSoup


def extract_links_with_regex(file_path, url_pattern):
    with open(file_path, 'r', encoding='utf8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    links = set()

    for a in soup.find_all('a', href=True):
        if re.match(url_pattern, a['href']):
            links.add(a['href'])

    return links


def extract_from_folder(folder_path, url_pattern):
    all_links = set()
    for file_path in glob.glob(f"{folder_path}/*.html"):
        file_links = extract_links_with_regex(file_path, url_pattern)
        all_links.update(file_links)
    return all_links


# Define the folder path and the regex pattern for the URLs
folder_path = 'C:\\Users\\liviuxyz\\Downloads\\Auto\\Pages'  # Replace with your folder path
url_pattern = r'https://www\.imobiliare\.ro/vanzare-garsoniere/[^/]+/[^/]+'

# Extract links from all .html files in the folder
unique_links = extract_from_folder(folder_path, url_pattern)

# Export to CSV
csv_file = "extracted_links.csv"
with open(csv_file, 'w', newline='', encoding='utf8') as file:
    writer = csv.writer(file)
    for link in unique_links:
        writer.writerow([link])

print(f"Extracted {len(unique_links)} unique links.")
