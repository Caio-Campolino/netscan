# NetScan

NetScan is a command-line network scanning tool developed in Python, inspired by the Nmap output format.
The project is focused on studying socket programming, clean code organization, and extensibility for use in controlled environments.

## Project Structure

```text
scanner_rede/
├── netscan                 # Entry point (Executable)
├── requirements.txt        # Dependencies
├── README.md
└── netscan_pkg/            # Main package
    ├── banner.py
    ├── core/               # Discovery logic
    └── utils/              # Loggers and helpers
```
---

## Installation and Usage

1. Quick setup:
```text
   git clone https://github.com/Caio-Campolino/netscan
   cd netscan
   pip install -r requirements.txt
   chmod +x netscan
```
2. Execution examples:
```text
 Basic Scan
./netscan 192.168.0.1

 Verbose Mode
./netscan 192.168.0.1 -v

 Help
./netscan -h
```
---
## Legal Disclaimer
This tool was developed strictly for educational purposes.
The author assumes no responsibility for misuse or for executing scans against networks without explicit authorization.
