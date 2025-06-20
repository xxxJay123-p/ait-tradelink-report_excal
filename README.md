# TRLinkHelper

## Overview

TRLinkHelper is a Python-based GUI application designed to automate the processing of Tradelink bill Excel files, Cargowise Excel/CSV reports, and optional HTML files. It matches transaction data between Tradelink and Cargowise, generates detailed reports, and supports a bilingual (English/Chinese) interface. Key features include:

- **Excel/CSV Processing**: Matches Tradelink bill transactions with Cargowise data.
- **HTML Parsing**: Extracts transaction details from HTML files and integrates them into Excel reports.
- **Progress Tracking**: Displays a progress bar with percentage updates during processing.
- **Bilingual Support**: Allows switching between English and Chinese interfaces.
- **Error Logging**: Logs processing details and errors to `trlink_helper.log`.

Developed by [xxxJay123](https://github.com/xxxJay123), this tool streamlines trade bill reconciliation for logistics and trade professionals.

## Installation

### Prerequisites
- Python 3.8 or higher
- Required Python libraries:
  ```bash
  pip install ttkbootstrap pandas openpyxl beautifulsoup4 chardet
  ```

### Setup
1. Clone or download the repository:
   ```bash
   git clone https://github.com/xxxJay123-p/ait-tradelink-report_excal.git
   cd trlinkhelper
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Create a `requirements.txt` with the following content:
   ```
   ttkbootstrap
   pandas
   openpyxl
   beautifulsoup4
   chardet
   ```
3. Ensure `trlinkhelper.ico` is in the project directory (optional, for Windows icon display).
4. Run the application:
   ```bash
   python trlink_helper.py
   ```

## Usage Guide

### Launching the Application
1. Run `python trlink_helper.py` to open the GUI.
2. The interface defaults to Chinese. Click "Switch to English" in the top-right corner to change to English.

### Step 1: Input Files
1. **Tradelink Bill (Excel)**: Click "Browse" to select a Tradelink bill Excel file (`.xlsx`). This file is required.
2. **Cargowise Data (Excel/CSV)**: Click "Browse" to select a Cargowise report in Excel (`.xlsx`) or CSV (`.csv`) format. This file is required.
3. **HTML File (Optional)**: Click "Browse" to select an HTML file containing transaction details, if applicable.

### Step 2: HTML Processing Settings
1. **Use "After Cut-Off" Algorithm**: Check this box (default: enabled) to process HTML data using the "EDI Transactions Since Last Charge Calculation" table. Uncheck to use the `soadetail` table parsing method.
2. **TDEC Transaction Amount**: Enter the TDEC transaction amount (default: 16.6). This value is used for HTML transaction calculations.

### Step 3: Output Settings
1. **Output File**: The default output file is `Tradelink_Bill_Report_<Current_Month>.xlsx`. Click "Save As" to choose a custom file name or location.
2. If the output file already exists, a prompt will ask whether to overwrite it.

### Processing
1. Click "Start Processing" to begin. A progress bar with a percentage label will appear, updating from 0% to 100%.
2. The log area at the bottom displays processing status, such as "Processing HTML file..." or "Processing Excel matching...".
3. Upon completion, a success message shows the output file path. If processing fails, an error message is displayed.

### Additional Features
- **Language Toggle**: Switch between English and Chinese using the top-right button.
- **Help Guide**: Click "Help Guide" to open the online documentation (replace `https://your-gitbook-url.com/trlinkhelper` with your actual URL).
- **ESC Button**: Click "ESC" to exit the application.
- **Error Logging**: Check `trlink_helper.log` for detailed processing logs.

### Output
The output Excel file contains:
- **Transaction Details**: Updated with HTML data (if provided).
- **Tradelink Matching Results**: Tradelink transaction details with match status.
- **Cargowise Matching Results**: Cargowise transaction details with match status.

## Troubleshooting

- **Progress Bar Not Showing**: Ensure valid Tradelink and Cargowise files are selected. Check `trlink_helper.log` for errors.
- **File Encoding Issues**: The app uses `chardet` to detect CSV encodings. If errors occur, verify the Cargowise CSV is UTF-8 or another supported encoding.
- **Missing Columns**: Ensure Cargowise files have columns for transaction number, outstanding amount, and job number (case-insensitive).
- **Icon Error (Windows)**: If `trlinkhelper.ico` is missing, remove `self.root.iconbitmap('trlinkhelper.ico')` from the code.
- **Dependencies**: Confirm all required libraries are installed (`ttkbootstrap`, `pandas`, `openpyxl`, `beautifulsoup4`, `chardet`).
- **Contact**: For issues, check the log file and contact the developer at [jay6677884@gmail.com]/[jcheng@aitworldwide.com].

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.