import csv

import requests
from bs4 import BeautifulSoup

url = 'https://gse.com.gh/listed-companies/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table')
csv_file = "company_data.csv"

if table:
    rows = table.find_all('tr')

    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)

        for row in rows:
            cells = row.find_all(['th', 'td'])

            row_data = [cell.get_text(strip=True) for cell in cells]

            csv_writer.writerow(row_data)

    print("Data written to successfully.")
else:
    print("Table not found on the webpage.")
