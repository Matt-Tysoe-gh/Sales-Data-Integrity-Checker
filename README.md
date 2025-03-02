# Sales Data Accuracy Tester
## Overview:
This project is a Python script that serves as a Sales Data Integrity Checker. It compares multiple Excel files containing sales data to ensure consistency and integrity. The script checks that each file has matching store IDs and compares the "Sell Out" totals on both a per-store basis and overall, reporting any discrepancies found.

## Features:
- Store ID Verification: Ensures all files share the same unique store IDs.
- Detailed Comparison: Compares "Sell Out" totals for each store as well as the overall totals.
- User-Friendly Output: Prints formatted results with comma-separated numbers for improved readability.
- Modular Design: Uses functions for clarity and easy maintenance.
- Efficient Data Processing: Utilizes pandas and groupby for quick and reliable calculations.

## Technologies Used:
- Python: Core programming language.
- Pandas: For data manipulation and analysis.
- OS & Itertools: For file handling and processing combinations of files.

## Setup and Installation:
### Prerequisites:

Python 3.6 or higher.
- Pandas library (install via pip install pandas).

Clone the Repository:
```
git clone https://github.com/DavePasta/Sales-Data-Integrity-Checker.git
```
### Prepare Your Data:

- Create a folder (e.g., Sales Data Files) and add your Excel files (with .xlsx or .xls extensions) containing the sales data.
- The file names indicate the expected outcome of the comparison. "C" stands for "Correct", meaning the file should match others in the comparison, while "W" stands for "Wrong", meaning the file is expected to mismatch when compared.

### Configure the Script:

- Open the script file (e.g., sales_data_integrity_checker.py) and update the base_file_path variable with the full path to your data folder.

### Run the Script:

python sales_data_integrity_checker.py
- The script will process the files, compare the sales data, and print the results in the console.

## Expected Outcome

This can be found in the "Expected Outcome.txt" file

## Roadmap:
- Enhanced Reporting: Implement functionality to output a summary report (CSV/Excel) for further analysis.
- Improved Error Handling: Add robust error checking for file I/O and data consistency.
- Automated Testing: Develop unit tests to ensure each component works as expected.
