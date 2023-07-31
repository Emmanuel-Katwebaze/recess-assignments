# pip install beautifulsoup4
# xeno-canto.org
# ebird.org

# Import libraries
# bs4 import BeautifulSoup # import BeautifulSoup library

# import requests # fetches the HTML content

from bs4 import BeautifulSoup
import requests

url = 'http://xeno-canto.org'
response = requests.get(url)

# Get title of the website

soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find('title')

print(title)

# Today's assignments
# Extract all bird species from this website url https://xeno-canto.org and generate
# the csv file or the JSON file format for the bird species, family and more
# Extract all bird songs from this website url https://xeno-canto.org
# use this API to get data. The endpoint for the webservice is at https://xeno-canto.org/api/2/recordings

# git config --global user.name "Emma"
# git config --global user.email "emmakatwebaze2@gmail.com"

# import csv
# import json
# from bs4 import BeautifulSoup
# import requests

# url = 'https://xeno-canto.org/api/2/recordings?query=cnt:brazil'
# response = requests.get(url)
# print(response.content)

import csv
import json
import requests

url = 'https://xeno-canto.org/api/2/recordings?query=cnt:brazil'
response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.content)
    records = data['recordings']

    # CSV file name
    csv_file = 'xeno_canto_records.csv'

    # CSV header fields
    header = ["id", "gen", "sp", "en", "rec", "cnt", "loc", "lat", "lng", "alt", "type", "sex", "stage", "method",
              "url", "file", "file-name", "lic", "q", "length", "time", "date", "uploaded", "also", "rmk",
              "bird-seen", "animal-seen", "playback-used", "temp", "regnr", "auto", "dvc", "mic", "smp"]

    # Write the data to the CSV file
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        csv_writer = csv.DictWriter(f, fieldnames=header)
        csv_writer.writeheader()

        # Filter the records to include only the desired fields
        filtered_records = [{k: v for k, v in record.items() if k in header} for record in records]
        csv_writer.writerows(filtered_records)

    print(f"Data extracted and saved to '{csv_file}'")
else:
    print("Error: Unable to fetch data from the API.")

import requests
import csv
import json
from bs4 import BeautifulSoup

# Function to extract bird species from the website


def extract_bird_species():
    url = 'https://xeno-canto.org/collection/species/latest'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Implement web scraping logic here to extract bird species
        species_list = soup.find_all('table', class_='results')
        species_data = []
        for species_table in species_list:
            common_names = species_table.find_all(
                'span', class_='common-name')
            sci_names = species_table.find_all(
                'span', class_='sci-name')
            for common_name, sci_name in zip(common_names, sci_names):
                species_data.append(
                    {'common_name': common_name.text.strip(), 'sci_name': sci_name.text.strip()})
        return species_data
    else:
        print('Failed to fetch data from the website.')
        return []

# Function to generate CSV file


def generate_csv(data):
    csv_filename = 'bird_species.csv'
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['common_name', 'sci_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Function to generate JSON file


def generate_json(data):
    json_filename = 'bird_species.json'
    with open(json_filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    bird_species_data = extract_bird_species()
    if bird_species_data:
        generate_csv(bird_species_data)
        generate_json(bird_species_data)
        print('CSV and JSON files generated successfully.')



