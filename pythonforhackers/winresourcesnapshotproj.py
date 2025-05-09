
# Created 05/09/2025
# Author: https://github.com/codewarrior0007
# Script Name: winresourcesnapshotproj.py
# Script Version: 1.0
# Scripting Language: Python 3.10
# Library used: psutil, socket, getpass, datetime
# Scripting Tool: Visual Studio Code
# Purpose: This script uses above mentioned libraries to collect Windows System snapshot _
# to later analysis
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

# # Aggregate all forensic snapshots
def collect_forensic_snapshot():
     forensic_data = {
        "user_info": get_user_info(),
         "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     }
    
     return forensic_data

## Main to print forensics snapshot
if __name__ == "__main__":
     print(collect_forensic_snapshot())