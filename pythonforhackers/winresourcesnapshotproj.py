# Created 05/11/2025
# Author: https://github.com/codewarrior0007
# Script Name: winresourcesnapshotproj.py
# Script Version: 1.0
# Scripting Language: Python 3.12
# Library used: psutil, socket, getpass, datetime
# Scripting Tool: Visual Studio Code
# Purpose: This script uses above mentioned libraries to collect Windows System snapshot _
# for later analysis
# Disclaimer: This script was written for demonstation purposes only. Any miss use of this _
# script is not the responsibility of the author.  

import psutil 
import socket
import getpass 
from datetime import datetime

# # Function to capture user account details
def get_user_info():
    user_info = {
        "username" : getpass.getuser(),
        "hostname" : socket.gethostname(),
        "users" : psutil.users() 
     }
    return user_info

# # Function to capture memory usage
def get_memory_snapshot():
    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()
    return {"virtual_memory": memory._asdict(), "swap_memory": swap._asdict()}

# # Function to capture running processes
def get_process_snapshot():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
        processes.append(proc.info)
    return processes

# # Aggregate all forensic snapshots
def collect_forensic_snapshot():
     forensic_data = {
        "user_info": get_user_info(),
        "memory_snapshot": get_memory_snapshot(),
        "process_snapshot": get_process_snapshot(), 
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     }
    
     return forensic_data

## Main to print forensics snapshot
if __name__ == "__main__":
     print(collect_forensic_snapshot())
