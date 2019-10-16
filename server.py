"""
Project 1 CSE 5344 Fall 2019
@author Ankit Khanna
UTA ID: 1001553616
"""

from socket import *

import threading


class ClientThread(threading.Thread):
    def __init__(self, connect, address):
        threading.Thread.__init__(self)
        self.connectionSocket = connect
        self.addr = address

    def run(self):
        while True:
            try:
                message = connectionSocket.recv(1024).decode()
                if not message:
                    break
                print("Request:\n", message)
                file_name = message.split()[1]
                if file_name is "/":
                    file_name = "/index.html"
                f = open(file_name[1:])
                # Read content of requested file
                outputdata = f.read()
                print("Output:\n", outputdata)

                # Send one HTTP header line into socket
                header_line = "HTTP/1.1 200 OK\r\n"
                header_info = {
                    "Content-Length": len(outputdata),
                    "Keep-Alive": "timeout=%d,max=%d" % (10, 100),
                    "Connection": "Keep-Alive",
                    "Content-Type": "text/html"
                }

                header_body = "\r\n".join("%s:%s" % (item, header_info[item]) for item in header_info)
                connectionSocket.send(("%s\r\n%s\r\n\r\n" % (header_line, header_body)).encode())

                # Send the content of the requested file to the client
                connectionSocket.send(outputdata.encode())
                connectionSocket.close()
                break
            except IOError:
                # Send response message for file not found
                connectionSocket.send("HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"
                                      "<!DOCTYPE html>\r\n<html>\r\n    <body>\r\n  <h1>404 Not Found<h1>\r\n"
                                      "   </body>\r\n</html>".encode())
                connectionSocket.close()
                break


if __name__ == '__main__':
    # Create a socket
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Port server will serve requests on
    serverPort = 6789
    # Bind the socket with host and port
    serverSocket.bind(('', serverPort))
    # Listen to incoming connections and have some buffer
    serverSocket.listen(5)
    threads = []
    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        print("Connected established with: ", addr)
        client_thread = ClientThread(connectionSocket, addr)
        client_thread.start()
        threads.append(client_thread)

    serverSocket.close()
