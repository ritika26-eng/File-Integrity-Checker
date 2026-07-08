File Integrity Checker

A cybersecurity project that monitors file integrity using **SHA-256 hashing**.  
The tool detects file modifications, deleted files, and newly added files by comparing current file hashes with previously stored hashes.

Features
- Generate SHA-256 file hashes
- Store hash values in a JSON database
- Verify file integrity
- Display file details (name, size, modified time, hash)
- Scan entire folders
- Detect modified files
- Detect deleted files
- Detect new files
- Generate integrity reports
- Color-coded terminal output
- Automatic folder monitoring

Technologies Used
- Python
- SHA-256 Cryptographic Hashing
- JSON File Handling
- File System Monitoring
- Colorama Library

Project Structure
File Integrity Checker
│
├── file_integrity_checker.py 
├── hashes.json 
├── integrity_report.txt
├── README.md
└── .gitignore

Installation
Clone the repository:
```bash
git clone <repository-url>
Install required library:
pip install colorama
▶️ How to Run
Run the program:
py file_integrity_checker.py

Working
The program calculates the SHA-256 hash of files.
Hash values are stored in a JSON database.
During scanning, current hashes are compared with previous hashes.
The tool identifies:
Unchanged files
Modified files
Deleted files
New files

Example Output
========== Integrity Report ==========

✓ test2.txt : Unchanged
✗ test1.txt : Modified
+ test3.txt : New File

✓ Scan completed.

Learning Outcomes
Cryptographic hashing concepts
File integrity monitoring (FIM)
Python automation
File system operations
Cybersecurity fundamentals