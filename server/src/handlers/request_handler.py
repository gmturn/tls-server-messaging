import ssl
import socket

class RequestHandler:
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address

    def handle_request(self):
        print(f"Connected to {self.connection}")

        c_Message = self.connection.read()
        
        while c_Message:
            print(f"IP {self.address}: '{c_Message}'")
            s_Message = str(input("Response: "))
            self.connection.send(s_Message)
            c_Message = self.connection.read()
        
        print(f"Connection with IP {self.address} has been terminated. Closing secure socket.")
        self.connection.close()
