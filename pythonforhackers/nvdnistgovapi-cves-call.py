# Created 05/03/2025
# Author: https://github.com/codewarrior0007
# Script Name: nvdnistgovapi-cves-call.py
# Script Version: 1.0
# Scripting Language: Python 3.10
# Library used: requests
# Input : CVE ID (e.g., CVE-2025-46558)
# Output: Full JSON response containing CVE details
# API Documentation: https://nvd.nist.gov/developers/start-here
# Scripting Tool: Visual Studio Code
# Purpose: This script fetches CVE details from the NVD API v2.0 using the requests _
# library for a given Input CVE.  
# Disclaimer: This script was written for demonstation purposes only. Any miss use of this _
# script is not the responsibility of the author.  


# Using Python requests library to call the NVD API v2.0 for CVE details
import requests

# NVD API endpoint (v2.0)
NVD_API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

# Function to fetch CVE details 
def get_cve_details(cve_id):
    """Fetch CVE details from NVD API v2.0."""
    params = {"cveId": cve_id}  # Correct parameter for querying a specific CVE
    response = requests.get(NVD_API_URL, params=params)
    # Check if the request was successful with status code 200
     
    if response.status_code == 200:
        return response.json()
    else: # Handle errors
        print(f"Error: Unable to fetch data (Status Code: {response.status_code})")
        return None

# Fetch CVE details
cve_data = get_cve_details("CVE-2025-46558")

# Print the full Jason response of CVE details
if cve_data:
    print(cve_data)  

