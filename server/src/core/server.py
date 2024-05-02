import server.src.utilities.config_loader as conf
from server.src.utilities import all


import socket
import ssl

class Server:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = conf.load_config(self.config_path)

        # INITIALIZE
        self.port = int(self.config['DEFAULT']['Port'])
        self.d_pubKey = self.config['DEFAULT']['CertificatePath']
        self.d_privKey = self.config['DEFAULT']['PrivateKeyPath']
        b_generateNewKeys = bool(self.config['DEFAULT']['GenerateNewKeys'])

        if b_generateNewKeys:
            pass

