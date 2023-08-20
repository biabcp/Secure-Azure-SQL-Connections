# Secure-Azure-SQL-Connections

# Secure SQL Connections Automation

Automate the process of securing client connections to Azure SQL Database and SQL Managed Instance by enforcing the use of modern TLS versions and disabling vulnerable protocols and cipher suites.

## Features

- Enforce minimal TLS version on Azure SQL servers.
- Update connection settings for applications.
- Disable vulnerable protocols and ciphers on client machines.

## Prerequisites

- Python 3.x is installed.
- Windows operating system (for the provided script).

## Usage

1. **Clone this repository:**

   ```bash
   git clone https://github.com/your-username/Secure-SQL-Connections.git
   cd Secure-SQL-Connections

python disable_tls_ciphers.py

Run the script to disable vulnerable protocols and ciphers on client machines:
python disable_tls_ciphers.py
Note: Run the script with administrative privileges.

Notes
Editing the Windows registry can have serious consequences. Use caution and back up the registry before making changes.
This project is intended to improve security by enforcing best practices.
Always test the script in a controlled environment before applying changes to production systems.
Use this project as a starting point for enhancing your organization's security measures.

Disclaimer: This project is provided as-is and is intended for educational and informational purposes only. The author and contributors are not responsible for any misuse, damages, or consequences arising from the use of this project.


