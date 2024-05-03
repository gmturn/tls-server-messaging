class TLSHandler:
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address

    def handle_request(self):
        print(f"Connected to {self.connection}")

        