"""
Project 1 CSE 5344 Fall 2019
@author Ankit Khanna
UTA ID: 1001553616
"""

from socket import *
import sys

host = sys.argv[1]
port = sys.argv[2]
file_name = ""
if len(sys.argv) is 4:
    filename = sys.argv[3]

host_port = "%s:%s" % (host, port)

try:
    # Create socket using TCP/IPv4
    client_socket = socket(AF_INET, SOCK_STREAM)
    # Establish Connection with server
    client_socket.connect((host, int(port)))
    # Prepare header for client request
    header = {
        "Request": "GET /%s HTTP/1.1" % file_name,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-us",
        "Host": host_port,
    }
    http_header = "\r\n".join("%s:%s" % (item, header[item]) for item in header)
    print(http_header)
    print("============================================================================")
    # Send Client Request
    client_socket.send(http_header.encode())
except IOError:
    sys.exit(1)

while True:
    data = client_socket.recv(1024)
    print(data.decode())
    if not data:
        break

# Close client socket
client_socket.close()
