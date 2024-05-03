class RequestHandler:
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address

    def handle_request(self):
        print(f"Connected to {self.connection}")

        try:
            while True:
                data = self.connection.recv(1024)
                if not data:
                    break  # No more data from client
                print(f"Received from {self.address}: {data.decode()}")
                self.connection.sendall(data)  # Echo back to client
        finally:
            self.connection.close()