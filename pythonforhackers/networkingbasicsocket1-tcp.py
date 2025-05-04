# Created 04/30/2025
# Author: https://github.com/codewarrior0007
# Script Name: networkingbasicsocket1-tcp.py
# Script Version: 1.0
# Scripting Language: Python 3.10
# Library used: socket
# Inputs : target_host (e.g., www.google.com), target_port (e.g., 80)
# Output: Response from the server in bytes and decoded string
# # Scripting Tool: Visual Studio Code
# Purpose: This script uses socket library to contact a site at port 80 and _
# gets the response from the server in the form of byters and decoded string.  
# Disclaimer: This script was written for demonstation purposes only. Any miss use of this _
# script is not the responsibility of the author.  

# # Using Python socket libreary to make a TCP connection to a server
import socket
 
target_host = 'www.google.com'
target_port = 80
 
# # # Create a socket object - AF_INET is for IPv4, SOCK_STREAM is for TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# # # Connect the client-socket to the target host and port
client.connect((target_host, target_port))
 
## # Send some data- HTTP GET request
client.send(b'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n')
 
# # # Receive some data- 4096 bytes
response = client.recv(4096)
 
 
print("Response  :",response)
# # Decode the response to a string
print("Decoded Response  :",response.decode()) 
 
### ==============================================

# Enhanced version of the above script.  Make sure to comment out the _
# above script before running the one below. This script uses loops and _
# context manager to ensure proper cleanup of the socket. It also handles _
# exceptions and sets a timeout for the connection attempts. The response _
# is received in chunks to ensure complete data retrieval. The response is _
# printed as bytes and as a decoded string.
import socket

target_host = "www.google.com"
target_port = 80

# # Use a context manager to ensure proper cleanup of the socket
try:
     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
         client.settimeout(5)  # Set a timeout for connection attempts

#         # Connect the client socket to the target host and port
         client.connect((target_host, target_port))

#         # Send HTTP GET request with proper line endings
         request = "GET / HTTP/1.1\r\nHost: google.com\r\nConnection: close\r\n\r\n"
         client.send(request.encode())

#         # Receive the complete response in chunks
         response = b""
         while True:
             chunk = client.recv(4096)
             if not chunk:
                 break
             response += chunk

#         # Print response as bytes and as a decoded string
         print("Response (bytes):", response)
         print("Decoded Response:", response.decode("utf-8", errors="ignore"))

# # Handle potential exceptions
except socket.timeout:
     print("Connection timed out!")
except socket.error as err:
     print(f"Socket error: {err}")
except Exception as e:
     print(f"An unexpected error occurred: {e}")
