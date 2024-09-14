import mailbox
from collections import Counter
import re
import os
import csv
import tkinter as tk
from tkinter import filedialog, messagebox

def extract_email_address(from_header):
    match = re.search(r'<(.+?)>', from_header)
    if match:
        return match.group(1)
    else:
        return from_header

def extract_email_domain(email_address):
    return email_address.split('@')[-1]

def analyze_mbox(file_path, email_counter, domain_counter):
    mbox = mailbox.mbox(file_path)
    for message in mbox:
        from_header = message['From']
        if from_header:
            email_address = extract_email_address(from_header)
            email_counter[email_address] += 1
            domain = extract_email_domain(email_address)
            domain_counter[domain] += 1

def analyze_single_file(file, email_counter, domain_counter):
    analyze_mbox(file, email_counter, domain_counter)
    most_common_senders = email_counter.most_common()
    most_common_domains = domain_counter.most_common()
    
    # Extract the base filename without extension
    base_filename = os.path.splitext(os.path.basename(file))[0]
    email_csv_filename = f"{base_filename}_email.csv"
    domain_csv_filename = f"{base_filename}_domain.csv"
    
    # Export results to CSV files
    export_to_csv(email_csv_filename, most_common_senders, ["Email Address", "Total Emails"])
    export_to_csv(domain_csv_filename, most_common_domains, ["Email Domain", "Total Emails"])

def analyze_multiple_files(files, email_counter, domain_counter):
    for file in files:
        analyze_mbox(file, email_counter, domain_counter)
    
    most_common_senders = email_counter.most_common()
    most_common_domains = domain_counter.most_common()
    
    # Common filenames for multiple files
    merged_email_csv_filename = "merged_email_counts.csv"
    merged_domain_csv_filename = "merged_domain_counts.csv"
    
    # Export results to CSV files
    export_to_csv(merged_email_csv_filename, most_common_senders, ["Email Address", "Total Emails"])
    export_to_csv(merged_domain_csv_filename, most_common_domains, ["Email Domain", "Total Emails"])

def open_files():
    files = filedialog.askopenfilenames(filetypes=[("MBox files", "*.mbox")])
    if files:
        files_label.config(text=f"Selected Files: {', '.join(os.path.basename(f) for f in files)}")
        analyze_button.config(state=tk.NORMAL)
        file_paths.set(files)

def analyze():
    files = file_paths.get()
    if not files:
        messagebox.showwarning("Warning", "No files selected.")
        return

    email_counter = Counter()
    domain_counter = Counter()

    if len(files) == 1:
        # Analyze the single file
        analyze_single_file(files[0], email_counter, domain_counter)
    else:
        # Analyze multiple files
        analyze_multiple_files(files, email_counter, domain_counter)
    
    messagebox.showinfo("Info", "Analysis completed and results exported.")

def export_to_csv(filename, data, headers):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for row in data:
            writer.writerow(row)

def setup_gui():
    global files_label, analyze_button, file_paths

    root = tk.Tk()
    root.title("Email Analyzer")

    # File selection
    tk.Label(root, text="Select .mbox Files:").pack(pady=5)
    tk.Button(root, text="Browse", command=open_files).pack(pady=5)

    files_label = tk.Label(root, text="No files selected")
    files_label.pack(pady=5)

    # Analyze button
    analyze_button = tk.Button(root, text="Analyze", command=analyze, state=tk.DISABLED)
    analyze_button.pack(pady=20)

    # Global variable for file paths
    file_paths = tk.Variable(value=[])

    root.mainloop()

if __name__ == "__main__":
    setup_gui()
