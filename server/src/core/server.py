import utilities.config_loader as conf
import utilities.load_keys as keys
import socket
import ssl

class Server:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = conf.load_config(self.config_path)

        # INITIALIZE
        self.port = int(self.config['DEFAULT']['Port'])
        self.d_pubKey = self.config['DEFAULT']['CertificateKeyPath']
        self.d_privKey = self.config['DEFAULT']['PrivateKeyPath']
        b_generateNewKeys = bool(self.config['DEFAULT']['GenerateNewKeys'])

        print(b_generateNewKeys)

        #self.pubKey, self.privKey = keys.load_keys(self.config['DEFAULT']['CertificatePath'], self.config['DEFAULT']['PrivateKeyPath'])
