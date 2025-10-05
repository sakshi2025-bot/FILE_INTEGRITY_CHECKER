"""
==========================================================
        FILE INTEGRITY CHECKER  🔐  
==========================================================

📘 Internship: CodTech Solutions – Task 1
👩‍💻 Developed by: Sakshi
🗓️ Project Title: File Integrity Checker
📁 Description:
    This Python script monitors changes in files by 
    calculating and comparing cryptographic hash values. 
    It helps ensure the integrity of important files and 
    detect any unauthorized modifications, deletions, or additions.

⚙️ Features:
    - Calculates file hash values using hashlib
    - Detects changed, missing, or newly added files
    - Stores hash data in JSON format
    - Simple menu-based interface

📚 Libraries Used:
    - os
    - hashlib
    - json
    - datetime

==========================================================
"""

import os
import hashlib
import json
from datetime import datetime

# ---------- Configuration ----------
HASH_ALGORITHM = 'sha256'       # Supported: md5, sha1, sha256, etc.
RECORD_FILE = 'file_hashes.json'  # File to store hash data
TARGET_FOLDER = 'files_to_monitor'  # Folder to monitor
# -----------------------------------


def calculate_hash(file_path, algorithm=HASH_ALGORITHM):
    """Calculate hash for a given file."""
    h = hashlib.new(algorithm)
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                h.update(chunk)
        return h.hexdigest()
    except FileNotFoundError:
        return None


def load_hash_records():
    """Load stored hash records from JSON file."""
    if not os.path.exists(RECORD_FILE):
        return {}
    with open(RECORD_FILE, 'r') as f:
        return json.load(f)


def save_hash_records(records):
    """Save hash records to JSON file."""
    with open(RECORD_FILE, 'w') as f:
        json.dump(records, f, indent=4)


def initialize_monitor():
    """Generate and store initial hash records."""
    records = {}
    for root, _, files in os.walk(TARGET_FOLDER):
        for name in files:
            file_path = os.path.join(root, name)
            file_hash = calculate_hash(file_path)
            records[file_path] = {
                'hash': file_hash,
                'last_checked': str(datetime.now())
            }
    save_hash_records(records)
    print(f"\n✅ Initial hashes saved for {len(records)} file(s).")
    print(f"📂 Hash record file created: {RECORD_FILE}")


def check_integrity():
    """Compare current file hashes with stored hashes."""
    records = load_hash_records()
    changed_files, missing_files, new_files = [], [], []

    # Calculate current hashes
    current_files = {}
    for root, _, files in os.walk(TARGET_FOLDER):
        for name in files:
            file_path = os.path.join(root, name)
            current_files[file_path] = calculate_hash(file_path)

    # Compare with stored records
    for file_path, old_data in records.items():
        old_hash = old_data['hash']
        new_hash = current_files.get(file_path)
        if new_hash is None:
            missing_files.append(file_path)
        elif old_hash != new_hash:
            changed_files.append(file_path)

    for file_path in current_files:
        if file_path not in records:
            new_files.append(file_path)

    # Display report
    print("\n==========================================================")
    print("🧩 FILE INTEGRITY CHECK REPORT")
    print("==========================================================")

    if not changed_files and not missing_files and not new_files:
        print("✅ All files are intact. No changes detected.")
    else:
        if changed_files:
            print("\n⚠️  Changed Files:")
            for f in changed_files:
                print("   -", f)
        if missing_files:
            print("\n❌ Missing Files:")
            for f in missing_files:
                print("   -", f)
        if new_files:
            print("\n🆕 New Files Detected:")
            for f in new_files:
                print("   -", f)

    # Update hash records after check
    for file_path in current_files:
        records[file_path] = {
            'hash': current_files[file_path],
            'last_checked': str(datetime.now())
        }
    save_hash_records(records)
    print("\n🕒 Integrity check completed and records updated.")
    print("==========================================================\n")


# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    os.makedirs(TARGET_FOLDER, exist_ok=True)

    print("""
==========================================================
            FILE INTEGRITY CHECKER 🔐
==========================================================
1. Initialize Monitor (Save initial file hashes)
2. Check File Integrity (Detect changes)
==========================================================
    """)

    choice = input("👉 Choose an option (1/2): ").strip()

    if choice == '1':
        initialize_monitor()
    elif choice == '2':
        check_integrity()
    else:
        print("❌ Invalid option. Exiting...")
