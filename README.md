# Email Analyzer - README

## Overview

The Email Analyzer is a Python-based tool that allows you to analyze `.mbox` files for email sender frequency and domain occurrence. It provides a graphical user interface (GUI) where you can select one or more `.mbox` files, run the analysis, and export the results into CSV files.

This tool can be used to gather insights into the most frequent email senders and the most commonly used domains in your email data. The results are saved into two CSV files: one for email addresses and another for email domains.

## Requirements

- **Python 3.x**
- **Libraries:**
  - `mailbox`: For reading `.mbox` files.
  - `collections.Counter`: For counting occurrences of email addresses and domains.
  - `re`: For extracting email addresses from headers.
  - `os`: For handling file paths and operations.
  - `csv`: For exporting data to CSV files.
  - `tkinter`: For the graphical user interface.
  
  These libraries are included in the Python standard library.

## Installation

No specific installation is required for the libraries since they are all part of Python's standard library. Just ensure you have Python 3 installed on your machine.

## Usage

1. **Run the script**: 
   - You can run the script from the terminal using:
     ```
     python email_analyzer.py
     ```
   - This will open a graphical user interface (GUI).

2. **Select .mbox files**:
   - Click the "Browse" button to open a file dialog.
   - You can select one or more `.mbox` files for analysis.

3. **Analyze**:
   - Once the files are selected, their names will be displayed in the interface.
   - Click the "Analyze" button to process the `.mbox` files.
   - The analysis will extract email addresses and domains from the `From` header of each email message.

4. **CSV Output**:
   - After the analysis completes, two CSV files will be generated:
     - One for email addresses and their counts.
     - One for email domains and their counts.
   - If analyzing multiple files, the CSVs will be merged across all files.

5. **Completion**:
   - After processing, a message box will notify you that the analysis is complete, and the results are exported.

## How the Code Works

### Core Functions

1. **extract_email_address(from_header)**: 
   - Extracts an email address from the `From` header using a regular expression. 
   - If no email address is found in angle brackets (`<>`), the raw header is returned.

2. **extract_email_domain(email_address)**: 
   - Splits an email address to extract the domain (part after `@`).

3. **analyze_mbox(file_path, email_counter, domain_counter)**: 
   - Reads an `.mbox` file and counts the occurrence of email addresses and their corresponding domains using `Counter`.

4. **analyze_single_file(file, email_counter, domain_counter)**:
   - Analyzes a single `.mbox` file and exports the results to CSV.

5. **analyze_multiple_files(files, email_counter, domain_counter)**:
   - Analyzes multiple `.mbox` files and exports combined results to CSV.

6. **export_to_csv(filename, data, headers)**:
   - Saves the analyzed data (email addresses/domains and their counts) to a CSV file with specified headers.

### GUI Setup

The user interface is created using `tkinter`:

- **File Selection**: 
  - A "Browse" button allows the user to select one or more `.mbox` files.
  - The selected file names are displayed in a label.

- **Analyze Button**: 
  - The "Analyze" button starts the analysis process. It becomes enabled once files are selected.

- **File Dialog**: 
  - Uses `filedialog.askopenfilenames` to let the user select `.mbox` files.

### Running the Application

The application is launched by calling the `setup_gui()` function, which sets up the interface and manages user interactions. Once files are selected and the analysis is complete, CSV files are generated based on the analysis.

### CSV File Naming

- For single files, the results are saved as `<filename>_email.csv` and `<filename>_domain.csv`.
- For multiple files, results are merged and saved as `merged_email_counts.csv` and `merged_domain_counts.csv`.

## Example

1. Select one or more `.mbox` files.
2. Click the "Analyze" button.
3. After completion, check your directory for CSV files that contain:
   - **Email Address Frequency** (`*_email.csv`)
   - **Domain Frequency** (`*_domain.csv`)

## License

Feel free to use and modify this tool for your personal or professional needs.

## Contributing

If you have any suggestions for improvements or find bugs, feel free to contribute by forking the repository and submitting a pull request.

## Contact

For any issues or questions, please reach out to the author via email.

---

Happy analyzing!
