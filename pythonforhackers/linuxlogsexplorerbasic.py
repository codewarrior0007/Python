# Created 05/05/2025
# Author: https://github.com/codewarrior0007
# Script Name: linuxlogsexplorer.py
# Script Version: 1.0
# Scripting Language: Python 3.10
# Library used: syslog, time
# Inputs : configuration file (e.g., config.json)
# Output: Response from the server in bytes and decoded string
# # Scripting Tool: Visual Studio Code
# Purpose: This script uses syslog library to send a test message to syslog and checks if it is logged correctly. _
# Disclaimer: This script was written for demonstation purposes only. Any miss use of this _
# script is not the responsibility of the author.  

# This script checks for a specific message in the syslog and prints the log entry if found. 

import syslog
import time

#Check if the message appears in the log
log_file = "/var/log/syslog"  # Adjust if logs are stored elsewhere

found = False
with open(log_file, "r") as file:
    logs = file.readlines()

# Search for the message and print the log entry if found
for line in logs:
    if "linuxlogsexplorerbasic" in line:
        print("Message logged:", True)
        print("Log entry:", line.strip())  # Print the exact log entry
        found = True
        break  # Stop searching after the first match

if not found:
    print("Message logged:", False)
