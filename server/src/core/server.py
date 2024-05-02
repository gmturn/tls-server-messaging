import server.src.utilities.config_loader as conf
from server.src.utilities import generate_keys, load_keys


import socket
import ssl

class Server:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = conf.load_config(self.config_path)

        # INITIALIZE
        self.port = int(self.config['DEFAULT']['Port'])
        self.d_PubKey = self.config['DEFAULT']['CertificatePath']
        self.d_PrivKey = self.config['DEFAULT']['PrivateKeyPath']
        b_generateNewKeys = bool(self.config['DEFAULT']['GenerateNewKeys'])

        # Generate new keys if stated in the config.conf file
        if b_generateNewKeys:
            generate_keys.generateNewKeys(self.d_PubKey, self.d_PrivKey)

        # Load keys from the public.pem and private.pem files
        self.PubKey, self.PrivKey = load_keys.loadKeys(self.d_PubKey, self.d_PrivKey)

        print(self.PubKey)
        print()
        print(self.PrivKey)

