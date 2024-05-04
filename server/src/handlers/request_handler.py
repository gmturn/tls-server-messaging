import ssl
import socket

class RequestHandler:
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address

    def handle_request(self):
        message = str(self.connection.recv(1024).decode())
        print(message)

        while message:
            response = str(input("Response: "))
            self.connection.sendall(response.encode())
            message = str(self.connection.recv(1024).decode())
                
        print(f"Connection with IP {self.address} has been terminated. Closing secure socket.")
        self.connection.close()
