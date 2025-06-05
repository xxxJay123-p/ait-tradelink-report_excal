import sys
import csv
import re
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class DragDropWidget(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setPlaceholderText("Drag and drop HTML file here")
        self.setReadOnly(True)
        # Increase size and font
        self.setFixedHeight(100)  # Larger height for drag-and-drop area
        self.setFont(QFont("Arial", 14))  # Larger font for placeholder text
        self.setStyleSheet("QLineEdit { padding: 10px; }")  # Add padding for better appearance

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for file in files:
            if file.lower().endswith('.html'):
                self.setText(file)
                event.accept()
                return
        QMessageBox.warning(self, "Invalid File", "Please drop an HTML file.")

class CSVGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tradelink Statement Helper|| By Jay")
        self.setFixedSize(600, 300)  # Increased window height to accommodate larger drag area

        # Main widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Drag and drop area
        self.file_input = DragDropWidget()
        layout.addWidget(QLabel("HTML File:"))
        layout.addWidget(self.file_input)

        # Checkbox for algorithm selection
        self.after_cutoff_cb = QCheckBox("Use 'After Cut-Off Time' Algorithm (uncheck for 'Before Cut-Off Time')")
        layout.addWidget(self.after_cutoff_cb)

        # Process button
        self.process_button = QPushButton("Generate CSV")
        self.process_button.clicked.connect(self.process_file)
        layout.addWidget(self.process_button)

        # Status label
        self.status_label = QLabel("Status: Ready")
        layout.addWidget(self.status_label)

    def process_file(self):
        html_file = self.file_input.text()
        if not html_file:
            self.status_label.setText("Status: Please drop an HTML file.")
            QMessageBox.warning(self, "No File", "Please drop an HTML file.")
            return

        try:
            with open(html_file, 'r', encoding='utf-8') as file:
                html_data = file.read()

            if self.after_cutoff_cb.isChecked():
                self.generate_csv_after_cutoff(html_data)
            else:
                self.generate_csv_before_cutoff(html_data)

        except FileNotFoundError:
            self.status_label.setText("Status: HTML file not found.")
            QMessageBox.critical(self, "Error", "HTML file not found.")
        except Exception as e:
            self.status_label.setText(f"Status: Error - {str(e)}")
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def generate_csv_before_cutoff(self, html_data):
        def parse_html_data(html_data):
            soup = BeautifulSoup(html_data, 'html.parser')
            table = soup.find('table', class_='soadetail')
            if not table:
                raise ValueError("No table with class 'soadetail' found.")

            rows = table.find_all('tr')
            structured_data = []
            for row in rows:
                cells = row.find_all('td')
                if len(cells) == 6:
                    item_description = cells[0].text.strip()
                    date = cells[1].text.strip()
                    unit_price_text = cells[2].text.strip('$ ')
                    unit = cells[3].text.strip()
                    qty_text = cells[4].text.strip()
                    net_amount_text = cells[5].text.strip('$ ')

                    try:
                        unit_price = float(unit_price_text)
                        qty = float(qty_text)
                    except ValueError:
                        continue

                    transaction_id = item_description.split(' (')[1].split(')')[0]
                    item_description = item_description.split(')')[1].strip()
                    form_type = ""
                    if "Form Type" in item_description:
                        try:
                            form_type = item_description.split("Form Type - ")[1]
                        except IndexError:
                            pass

                    year, month, day = date.split('/')
                    if "TDEC TRANSACTION" not in item_description:
                        transaction_type = "IMPORT/EXPORT DECLARATION CHARGE"
                        tdec_transaction = "16.6"
                        import_export_charge = str(unit_price)
                        tdec_clothing_levy = "0.0"
                        tdec_penalty = "0.0"
                        total = str(float(net_amount_text))

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
        header = ["Statement Date", "Transaction Date", "UXR", "Item Description", "EDI Address", "Party ID", "Form Type", "Internal Reference #1", "Internal Reference #2", "Internal Reference #3", "Internal Reference #4", "Internal Reference #5", "User", "TDEC Transaction", "Import/Export Declaration Charge", "TDEC Clothing Levy Charge", "TDEC Penalty Charge", "Total"]
        data.insert(0, header)

        if len(data) > 1:
            with open('tradelink_statement.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(data)
            self.status_label.setText("Status: CSV file generated: tradelink_statement.csv")
            QMessageBox.information(self, "Success", "CSV file generated: tradelink_statement.csv")
        else:
            self.status_label.setText("Status: No data to write to CSV.")
            QMessageBox.warning(self, "No Data", "No data to write to the CSV file.")

    def generate_csv_after_cutoff(self, html_data):
        soup = BeautifulSoup(html_data, 'html.parser')
        specific_td = None
        for td in soup.find_all('td', class_='header', colspan='6'):
            if 'EDI Transactions Since Last Charge Calculation' in td.get_text():
                specific_td = td
                break

        if specific_td:
            table = specific_td.find_parent('table')
            if table:
                data = []
                headers = [
                    'Transaction Date', 'UXR', 'Item Description', 'EDI Address', 'Party ID', 'Form Type',
                    'Internal Reference #1', 'Internal Reference #2', 'Internal Reference #3',
                    'Internal Reference #4', 'Internal Reference #5', 'User', 'TDEC Transaction',
                    'Import/Export Declaration Charge', 'TDEC Clothing Levy Charge', 'TDEC Penalty Charge', 'Total'
                ]
                data.append(headers)

                current_row = []
                for row in table.find_all('tr'):
                    cells = row.find_all(['td', 'th'])
                    if cells and not row.find('td', colspan='6'):
                        raw_row = [cell.get_text(strip=True) for cell in cells]
                        if 'Amount Paidby Subscriber' in raw_row or 'Transmission Date' in raw_row:
                            continue
                        new_row = [''] * len(headers)
                        if len(raw_row) >= 6:
                            new_row[0] = raw_row[4]  # Transaction Date
                            new_row[1] = raw_row[2]  # UXR
                            new_row[2] = "TDEC TRANSACTION"
                            new_row[3] = raw_row[0]  # EDI Address
                            new_row[4] = raw_row[0]  # Party ID
                            new_row[5] = raw_row[3]  # Form Type
                            new_row[11] = "tmka92634"  # User
                            new_row[13] = raw_row[5].replace('$', '') if len(raw_row) > 5 else ''  # Import/Export Declaration Charge
                            new_row[12] = '16.6'  # TDEC Transaction
                            try:
                                total = float(new_row[13]) + 16.6
                                new_row[16] = f'{total:.1f}'
                            except ValueError:
                                new_row[16] = ''
                        current_row = new_row
                        data.append(new_row)
                    elif cells and row.find('td', colspan='6'):
                        ref_text = cells[0].get_text(strip=True)
                        ref_matches = re.findall(r'Ref\. # \d+\s*-\s*([^\n<]+)', ref_text)
                        if current_row and len(data) > 1:
                            last_row = data[-1]
                            for i, ref in enumerate(ref_matches[:5]):
                                last_row[6 + i] = ref.strip()

                if len(data) > 1:
                    with open('edi_transactions.csv', 'w', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerows(data)
                    self.status_label.setText("Status: CSV file saved: edi_transactions.csv")
                    QMessageBox.information(self, "Success", "CSV file generated: edi_transactions.csv")
                else:
                    self.status_label.setText("Status: No data to write to CSV.")
                    QMessageBox.warning(self, "No Data", "No data to write to the CSV file.")
            else:
                self.status_label.setText("Status: No parent table found.")
                QMessageBox.critical(self, "Error", "No parent table found.")
        else:
            self.status_label.setText("Status: Specific <td> not found.")
            QMessageBox.critical(self, "Error", "Specific <td class='header' colspan='6'> not found.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CSVGeneratorApp()
    window.show()
    sys.exit(app.exec_())