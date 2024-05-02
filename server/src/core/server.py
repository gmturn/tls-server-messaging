import utilities.config_loader as conf
import socket
import ssl

class Server:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = conf.load_config(self.config_path)

    def initialize():
        pass
