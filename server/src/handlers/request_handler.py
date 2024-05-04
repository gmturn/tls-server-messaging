import ssl
import socket

class RequestHandler:
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address

    def handle_request(self):
        data = self.connection.recv(1024).decode()
        while data:
            print(f"IP [{self.address}]: '{data}'")
            response = str(input("Enter Response: "))
            
            try:
                self.connection.sendall(response.encode())
                data = str(self.connection.recv(1024).decode())
            except:
                print("Error: failed to send message to client.")
        

                
        print(f"Connection with IP {self.address} has been terminated. Closing secure socket.")
        self.connection.close()
