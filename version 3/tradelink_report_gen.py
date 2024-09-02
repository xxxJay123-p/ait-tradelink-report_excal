from bs4 import BeautifulSoup
import csv

with open('index.html', 'r') as file:
    html_data = file.read()

def parse_html_data(html_data):
    # Parse the HTML data using BeautifulSoup
    soup = BeautifulSoup(html_data, 'html.parser')

    # Find the table with the class "soadetail"
    table = soup.find('table', class_='soadetail')

    # Extract the data from the table
    rows = table.find_all('tr')
    structured_data = []

    for row in rows:
        cells = row.find_all('td')
        if len(cells) == 6:
            # Extract the data from the cells
            item_description = cells[0].text.strip()
            date = cells[1].text.strip()
            unit_price_text = cells[2].text.strip('$ ')
            unit = cells[3].text.strip()
            qty_text = cells[4].text.strip()
            net_amount_text = cells[5].text.strip('$ ')

            # Check if the unit price and quantity can be converted to float
            try:
                unit_price = float(unit_price_text)
                qty = float(qty_text)
            except ValueError:
                continue  # Skip this row if the data is not in the expected format

            # Extract the transaction ID and form type from the item description
            transaction_id = item_description.split(' (')[1].split(')')[0]
            item_description = item_description.split(')')[1].strip()
            form_type = ""
            if "Form Type" in item_description:
                try:
                    form_type = item_description.split("Form Type - ")[1]
                except IndexError:
                    pass  # Skip this row if the format is not as expected

            # Split the date into year, month, and day
            year, month, day = date.split('/')

            # Determine the transaction type
            if "TDEC TRANSACTION" not in item_description:
                transaction_type = "IMPORT/EXPORT DECLARATION CHARGE"
                tdec_transaction = "16.6"
                import_export_charge = str(unit_price)
                tdec_clothing_levy = "0.0"
                tdec_penalty = "0.0"
                total = str(float(net_amount_text))

                # Only add the row if the total is not 16.6
                if total != "16.6":
                    structured_data.append([
                        f"{year}/{month}/{day}",
                        date,
                        transaction_id,
                        item_description,
                        "39958258001.TL",
                        "39958258001.TL",
                        form_type,
                        "",
                        "",
                        "",
                        "",
                        "",
                        "tmka92634",
                        tdec_transaction,
                        import_export_charge,
                        tdec_clothing_levy,
                        tdec_penalty,
                        total
                    ])

    return structured_data

data = parse_html_data(html_data)

# Add the header row
header = ["Statement Date", "Transaction Date", "UXR", "Item Description", "EDI Address", "Party ID", "Form Type", "Internal Reference #1", "Internal Reference #2", "Internal Reference #3", "Internal Reference #4", "Internal Reference #5", "User", "TDEC Transaction", "Import/Export Declaration Charge", "TDEC Clothing Levy Charge", "TDEC Penalty Charge", "Total"]
data.insert(0, header)

# Iterate through the data rows
for row in data[1:]:
    transaction_date = row[1]
    uxr = row[2]
    item_description = row[3]
    tdec_transaction = float(row[13])
    form_type = row[6]
    import_export_declaration_charge = float(row[14])

    # Append the data to the list
    data.append({
        'Statement Date': row[0],
        'Transaction Date': transaction_date,
        'UXR': uxr,
        'Item Description': item_description,
        'EDI Address': row[4],
        'Party ID': row[5],
        'Form Type': form_type,
        'Internal Reference #1': row[7],
        'Internal Reference #2': row[8],
        'Internal Reference #3': row[9],
        'Internal Reference #4': row[10],
        'Internal Reference #5': row[11],
        'User': row[12],
        'TDEC Transaction': tdec_transaction,
        'Import/Export Declaration Charge': import_export_declaration_charge,
        'TDEC Clothing Levy Charge': 0.0,
        'TDEC Penalty Charge': 0.0,
        'Total': tdec_transaction + import_export_declaration_charge
    })

# Write the data to a CSV file
if len(data) > 1:
    with open('tradelink_statement.csv', 'w', newline='') as csvfile:
        fieldnames = data[0]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in data[1:]:
            if isinstance(row, dict):
                writer.writerow(row)

    print("CSV file generated: tradelink_statement.csv")
else:
    print("No data to write to the CSV file.")





