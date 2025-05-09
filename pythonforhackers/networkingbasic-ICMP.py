# Created 05/08/2025
# Author: https://github.com/codewarrior0007
# Script Name: networkingbasicsocket-ICMP.py
# Script Version: 1.0
# Scripting Language: Python 3.10
# Library used: scapy
# Inputs : target_host (e.g., www.google.com), target_port (e.g., 80)
# Output: Response from the server in bytes and decoded string
# # Scripting Tool: Visual Studio Code
# Purpose: This script uses scapy  library to contact to sent a ICPM request _
# Disclaimer: This script was written for demonstation purposes only. Any miss use of this _
# script is not the responsibility of the author.  

# # Using Python socket libreary to make a UDP connection to a server
from scapy.all import IP, ICMP, sr1

# Define the target
target = "www.google.com"

# Create and send an ICMP Echo Request (similar to a ping)
packet = IP(dst=target)/ICMP()
response = sr1(packet, timeout=2, verbose=False)

if response:
    print("Received response:")
    response.show()
else:
    print("No response received.")
