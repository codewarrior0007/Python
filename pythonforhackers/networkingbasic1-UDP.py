# Created 05/07/2025
# Author: https://github.com/codewarrior0007
# Script Name: networkingbasicsocket1-udp.py
# Script Version: 1.0
# Scripting Language: Python 3.10
# Library used: socket
# Inputs : target_host (e.g., www.google.com), target_port (e.g., 80)
# Output: Response from the server in bytes and decoded string
# # Scripting Tool: Visual Studio Code
# Purpose: This script uses socket library to contact a site at port 80 but _
# there is no since it's a UDP request.  
# Disclaimer: This script was written for demonstation purposes only. Any miss use of this _
# script is not the responsibility of the author.  

# # Using Python socket libreary to make a UDP connection to a server
import socket

target_host = 'www.google.com'
target_port = 80

# Create a socket object - AF_INET is for IPv4, SOCK_DGRAM is for UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data using sendto() method since UDP is connectionless
message = b'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n'
client.sendto(message, (target_host, target_port))

# Receive response using recvfrom()
response, addr = client.recvfrom(4096)

print("Response  :", response)
print("Decoded Response  :", response.decode())

# Close the socket
client.close()
