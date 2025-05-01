#TCP Client - Socket is a low-level networking interface in Python
# This example demonstrates how to create a TCP client that connects to a server, sends a request, and receives a response.
 import socket

 target_host = 'www.google.com'
 target_port = 80

# # Create a socket object - AF_INET is for IPv4, SOCK_STREAM is for TCP
 client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Connect the client-socket to the target host and port
 client.connect((target_host, target_port))

# # Send some data- HTTP GET request
 client.send(b'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n')

# # Receive some data- 4096 bytes
 response = client.recv(4096)


 print("Response  :",response)
# Decode the response to a string
 print("Decoded Response  :",response.decode()) 



# Enhanced version of the above script.  Make sure to comment out the above script before running the one below
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
