import csv
from bs4 import BeautifulSoup
import re

try:
    # Read the HTML file
    with open('index.html', 'r') as file:
        html_data = file.read()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_data, 'html.parser')

    # Debug: Print all <td> tags with colspan="6" to verify existence
    print("Debug: All <td> tags with colspan='6':")
    for td in soup.find_all('td', colspan='6'):
        print(f" - {td}")

    # Find the specific <td> with class="header" and colspan="6"
    specific_td = None
    for td in soup.find_all('td', class_='header', colspan='6'):
        if 'EDI Transactions Since Last Charge Calculation' in td.get_text():
            specific_td = td
            break

    # Check if the specific <td> was found
    if specific_td:
        print("\nFound the target <td>:", specific_td)

        # Find the parent table of the specific <td>
        table = specific_td.find_parent('table')
        if table:
            # Extract data from the table
            data = []
            headers = [
                'Transaction Date', 'UXR', 'Item Description', 'EDI Address', 'Party ID', 'Form Type',
                'Internal Reference #1', 'Internal Reference #2', 'Internal Reference #3',
                'Internal Reference #4', 'Internal Reference #5', 'User', 'TDEC Transaction',
                'Import/Export Declaration Charge', 'TDEC Clothing Levy Charge', 'TDEC Penalty Charge', 'Total'
            ]
            data.append(headers)  # Initialize with headers

            current_row = []
            for row in table.find_all('tr'):
                cells = row.find_all(['td', 'th'])
                if cells and not row.find('td', colspan='6'):  # Data row
                    raw_row = [cell.get_text(strip=True) for cell in cells]
                    # Skip unwanted header row containing 'Amount Paidby Subscriber'
                    if 'Amount Paidby Subscriber' in raw_row or 'Transmission Date' in raw_row:
                        continue
                    # Map raw columns (SID, ICR, Transaction ID / CAR, Charge Type, Transmission Date, Amount Paid by Subscriber)
                    new_row = [''] * len(headers)  # Initialize with empty strings
                    if len(raw_row) >= 6:
                        new_row[0] = raw_row[4]  # Transaction Date = Transmission Date
                        new_row[1] = raw_row[2]  # UXR = Transaction ID / CAR
                        new_row[2]= "TDEC TRANSACTION"
                        new_row[3] = raw_row[0]  # EDI Address = SID
                        new_row[4] = raw_row[0]
                        new_row[5] = raw_row[3]  # Form Type = Charge Type
                        new_row[11] = "tmka92634"
                        new_row[13] = raw_row[5].replace('$', '') if len(raw_row) > 5 else ''  # Import/Export Declaration Charge = Amount Paid by Subscriber
                        new_row[12] = '16.6'  # TDEC Transaction = 16.6
                        # Calculate Total = Import/Export Declaration Charge + TDEC Transaction
                        try:
                            total = float(new_row[13]) + 16.6
                            new_row[16] = f'{total:.1f}'  # Format to 1 decimal place
                        except ValueError:
                            new_row[16] = ''  # Leave empty if conversion fails
                    current_row = new_row
                    data.append(new_row)  # Append with empty refs initially
                elif cells and row.find('td', colspan='6'):  # Reference row
                    ref_text = cells[0].get_text(strip=True)
                    ref_matches = re.findall(r'Ref\. # \d+\s*-\s*([^\n<]+)', ref_text)
                    if current_row and len(data) > 1:  # Associate refs with last data row
                        last_row = data[-1]
                        for i, ref in enumerate(ref_matches[:5]):  # Limit to 5 refs
                            last_row[6 + i] = ref.strip()  # Internal Reference #1 to #5

            # Debug: Print extracted data
            print("\nExtracted table data:")
            for row in data:
                print(row)

            # Write the data to a CSV file
            with open('edi_transactions.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(data)

            print("\nCSV file saved: edi_transactions.csv")
        else:
            print("\nError: No parent table found for the target <td>.")
    else:
        print("\nError: Specific <td class='header' colspan='6'> with 'EDI Transactions Since Last Charge Calculation' not found.")

except FileNotFoundError:
    print("Error: 'index.html' file not found. Please ensure the file exists in the correct directory.")
except Exception as e:
    print(f"An error occurred: {str(e)}")