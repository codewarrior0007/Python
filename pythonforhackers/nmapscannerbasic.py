# Created 05/04/2025
# Author: https://github.com/codewarrior0007
# Script Name: nmapscanner.py
# Script Version: 1.0
# Scripting Language: Python 3.10
# Library used: nmap3 from https://github.com/nmmapper/python3-nmap
# Inputs : target_host (e.g., www.google.com)
# Output: Response from the server in json format
# # Scripting Tool: Visual Studio Code
# Purpose: This script uses nmap3 library to contact a site at and _
# gets the json response from the server for all the top open ports.  
# Disclaimer: This script was written for demonstation purposes only. Any miss use of this _
# script is not the responsibility of the author.  


 import nmap3

 nmap = nmap3.Nmap()
 target_host = "www.google.com"
 results = nmap.scan_top_ports(target_host)

 print(results)
