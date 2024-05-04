class RequestHandler:
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address

    def request_connection(self):
        self.connection.sendall("Client has connected.".encode())

        message = str(self.connection.recv(1024).decode())
        while message:
            
            print(f"Host [{self.address}]: '{message}'")

        
            response = str(input("Enter Response: "))
            self.connection.sendall(response.encode())
            message = str(self.connection.recv(1024).decode())
            
                
        print(f"Connection with Host {self.address} has been terminated. Closing secure socket.")
        self.connection.close()