import sys
import csv
import re
import json
import os
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox, QMessageBox
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QFont, QCursor, QIcon
from PyQt5.Qt import QDesktopServices

class DragDropWidget(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setPlaceholderText("Drag and drop HTML file here")
        self.setReadOnly(True)
        self.setFixedHeight(100)
        self.setFont(QFont("Arial", 14))
        self.setStyleSheet("QLineEdit { padding: 10px; }")

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
        self.setWindowTitle("Tradelink Statement Helper || By Jay")
        self.setWindowIcon(QIcon('app_icon.ico'))  # Set the window icon
        self.setFixedSize(600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        tdec_layout = QHBoxLayout()
        tdec_layout.addWidget(QLabel("TDEC Transaction Amount:"))
        self.tdec_input = QLineEdit()
        self.tdec_input.setFixedWidth(100)
        self.tdec_input.setFont(QFont("Arial", 12))
        tdec_layout.addWidget(self.tdec_input)
        self.save_tdec_button = QPushButton("Save Amount")
        self.save_tdec_button.clicked.connect(self.save_tdec_amount)
        tdec_layout.addWidget(self.save_tdec_button)
        tdec_layout.addStretch()
        layout.addLayout(tdec_layout)

        self.file_input = DragDropWidget()
        layout.addWidget(QLabel("HTML File:"))
        layout.addWidget(self.file_input)

        self.after_cutoff_cb = QCheckBox("Use 'After Cut-Off Time' Algorithm (uncheck for 'Before Cut-Off Time')")
        layout.addWidget(self.after_cutoff_cb)

        self.process_button = QPushButton("Generate CSV")
        self.process_button.clicked.connect(self.process_file)
        layout.addWidget(self.process_button)

        self.status_label = QLabel("Status: Ready")
        layout.addWidget(self.status_label)

        self.tdec_amount = "16.6"
        self.load_tdec_amount()
        self.check_tdec_reminder()

    def load_tdec_amount(self):
        config_file = "config.json"
        try:
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    config = json.load(f)
                    self.tdec_amount = str(config.get("tdec_amount", "16.6"))
                    self.tdec_input.setText(self.tdec_amount)
        except Exception as e:
            self.status_label.setText(f"Status: Error loading config - {str(e)}")
            QMessageBox.warning(self, "Config Error", f"Failed to load TDEC amount. Using default: {self.tdec_amount}")

    def save_tdec_amount(self):
        amount = self.tdec_input.text().strip()
        try:
            amount_float = float(amount)
            if amount_float <= 0:
                raise ValueError("Amount must be positive")
            self.tdec_amount = str(amount_float)
            config = {
                "tdec_amount": self.tdec_amount,
                "last_updated": datetime.now().strftime("%Y-%m-%d")
            }
            with open("config.json", 'w') as f:
                json.dump(config, f, indent=4)
            self.status_label.setText("Status: TDEC Transaction amount saved")
            QMessageBox.information(self, "Success", f"TDEC Transaction amount saved: {self.tdec_amount}")
        except ValueError as e:
            self.status_label.setText(f"Status: Invalid amount - {str(e)}")
            QMessageBox.warning(self, "Invalid Input", f"Please enter a valid positive number: {str(e)}")

    def check_tdec_reminder(self):
        config_file = "config.json"
        try:
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    config = json.load(f)
                    last_updated = config.get("last_updated")
                    if last_updated:
                        last_date = datetime.strptime(last_updated, "%Y-%m-%d")
                        if datetime.now() - last_date > timedelta(days=730):
                            QMessageBox.warning(self, "Reminder", "TDEC Transaction amount hasn’t been updated in over 2 years. Please review and save a new amount.")
        except Exception:
            pass

    def process_file(self):
        html_file = self.file_input.text().strip()
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
        soup = BeautifulSoup(html_data, 'html.parser')
        table = soup.find('table', class_='soadetail')
        if not table:
            raise ValueError("No table with class 'soadetail' found.")

        rows = table.find_all('tr')
        transactions = {}
        for row in rows:
            cells = row.find_all('td')
            if len(cells) != 6:
                continue

            item_description = cells[0].text.strip()
            date = cells[1].text.strip()
            net_amount_text = cells[5].text.strip().replace('$', '').strip()

            try:
                net_amount = float(net_amount_text)
            except ValueError:
                continue

            # Extract transaction ID
            transaction_id_match = re.search(r'\(([A-Z0-9]A39KJEA00[A-Z0-9]+)\)', item_description)
            if not transaction_id_match:
                continue
            transaction_id = transaction_id_match.group(1)

            # Initialize transaction data if not exists
            if transaction_id not in transactions:
                transactions[transaction_id] = {
                    'date': date,
                    'form_type': '',
                    'ref': '',
                    'tdec_transaction': 0.0,
                    'import_export_charge': 0.0,
                    'clothing_levy_charge': 0.0,
                    'penalty_charge': 0.0,
                    'total': 0.0
                }

            # Process item types
            if item_description.startswith('TDEC TRANSACTION'):
                transactions[transaction_id]['tdec_transaction'] = float(self.tdec_amount)
            elif item_description.startswith('IMPORT/EXPORT DECLARATION CHARGE'):
                transactions[transaction_id]['import_export_charge'] = net_amount
                form_type_match = re.search(r'Form Type\s*-\s*([^<\n]+)', cells[0].text)
                if form_type_match:
                    transactions[transaction_id]['form_type'] = form_type_match.group(1).strip()
            elif item_description.startswith('TDEC CLOTHING'):
                transactions[transaction_id]['clothing_levy_charge'] = net_amount
            elif item_description.startswith('TDEC PENALTY CHARGE'):
                transactions[transaction_id]['penalty_charge'] = net_amount
                ref_match = re.search(r'Ref\. # 1\s*-\s*([^<\n]+)', cells[0].text)
                if ref_match:
                    transactions[transaction_id]['ref'] = ref_match.group(1).strip()

            # Calculate total
            transactions[transaction_id]['total'] = (
                transactions[transaction_id]['tdec_transaction'] +
                transactions[transaction_id]['import_export_charge'] +
                transactions[transaction_id]['clothing_levy_charge'] +
                transactions[transaction_id]['penalty_charge']
            )

        # Format data for CSV
        structured_data = []
        for transaction_id, data in transactions.items():
            if data['total'] == float(self.tdec_amount):
                continue  # Skip if only TDEC TRANSACTION

            year, month, day = data['date'].split('/')
            structured_data.append([
                f"{year}/{month}/{day}",
                data['date'],
                transaction_id,
                "TDEC TRANSACTION",
                "39958258001.TL",
                "39958258001.TL",
                data['form_type'],
                data['ref'],
                "", "", "",
                "tmka92634",
                str(data['tdec_transaction']),
                str(data['import_export_charge']) if data['import_export_charge'] > 0 else "",
                str(data['clothing_levy_charge']) if data['clothing_levy_charge'] > 0 else "",
                str(data['penalty_charge']) if data['penalty_charge'] > 0 else "",
                str(data['total'])
            ])

        header = ["Statement Date", "Transaction Date", "UXR", "Item Description", "EDI Address", "Party ID", "Form Type", "Internal Reference #1", "Internal Reference #2", "Internal Reference #3", "Internal Reference #4", "User", "TDEC Transaction", "Import/Export Declaration Charge", "TDEC Clothing Levy Charge", "TDEC Penalty Charge", "Total"]
        structured_data.insert(0, header)

        if len(structured_data) > 1:
            with open('tradelink_statement.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(structured_data)
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
                            new_row[12] = self.tdec_amount  # Use stored amount
                            try:
                                total = float(new_row[13]) + float(self.tdec_amount)
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
                    self.status_label.setText("Status: CSV file generated: edi_transactions.csv")
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