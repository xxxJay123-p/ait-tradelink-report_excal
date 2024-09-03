import csv
from bs4 import BeautifulSoup

with open('index.html', 'r') as file:
    html_data = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_data, 'html.parser')

# Extract the data from the table
data = []
for row in soup.find_all('tr'):
    cells = row.find_all('td')
    if cells:
        row_data = [cell.text.strip() for cell in cells]
        # Remove the "Form Type - Export Form 2" text
        if len(row_data) == 6 and row_data[4] == '2024/08/30':
            row_data = row_data[:4] + row_data[5:]
        data.append(row_data)

# Write the data to a CSV file
with open('edi_transactions.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

print("CSV file saved: edi_transactions.csv")

