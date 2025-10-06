# FILE_INTEGRITY_CHECKER

*COMPANY*: CODTECH IT SOLUTIONS  

*NAME*: SAKSHI NAGARAJ MASHETTY

*INTERN ID*: CT06DY1830

*DOMAIN*: CYBERSECURITY AND ETHICAL HACKING 

*DURATION*: 4 WEEKS 

*MENTOR*: NEELA SANTHOSH


🧩 Task 1: File Integrity Checker

The File Integrity Checker is a Python-based tool designed to monitor changes in files and ensure data integrity. It helps detect any unauthorized or accidental modifications, additions, or deletions in important files within a directory. This kind of tool is crucial for maintaining system security and ensuring that critical files remain unaltered over time.

🔍 Objective

The main goal of this project is to develop a utility that can:

Calculate and store the cryptographic hash values (like SHA256) of files.

Periodically or manually verify files to check if their content has changed.

Alert the user if any file has been modified, deleted, or newly added.

⚙️ How It Works

Initial Scan:
The tool scans the selected directory and computes hash values for each file using a secure hashing algorithm.

Database Creation:
These hash values are stored in a reference file (like hashes.json) for future comparisons.

Integrity Verification:
During subsequent runs, the tool re-scans the directory, recalculates the hashes, and compares them with the stored ones.

Change Detection:
If discrepancies are found, it reports files that have been changed, removed, or added since the last scan.

💡 Key Features

Uses SHA256 for secure and reliable hashing.

Detects file modifications, deletions, and additions.

Saves results in a structured format (JSON or text).

Simple command-line interface for easy use.

🛠️ Technologies Used

Language: Python

Libraries: os, hashlib, json, and datetime

🧠 Practical Use

This tool can be applied in:

Monitoring system configuration files.

Detecting tampering in web or application files.

Ensuring backup integrity and version control.

🏁 Outcome

The project successfully demonstrates the use of file hashing and comparison techniques for security monitoring. It provides users with a simple yet effective way to ensure that critical files remain unchanged, supporting both system integrity and cybersecurity best practices.

#OUTPUT

<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/b4f7a779-ef89-4634-a778-6789426f5e7a" />


