#import server.src.utilities.config_loader as conf
from server.src.utilities import generate_keys, load_keys, read_whitelist
import server.src.utilities.config_loader as conf


import socket
import ssl
import select

class Server:
    def __init__(self, config_path):
        self.d_Config = config_path
        self.config = conf.load_config(self.d_Config)

        # INITIALIZE
        self.port = int(self.config['DEFAULT']['Port'])
        self.host = str(self.config['DEFAULT']['Host'])
        self.d_PubKey = self.config['DEFAULT']['CertificatePath']
        self.d_PrivKey = self.config['DEFAULT']['PrivateKeyPath']

        self.d_Log = self.config['DEFAULT']['LogPath']
        self.logging = self.config['DEFAULT']['Logging']
        self.b_Whitelist = bool(self.config['DEFAULT']['Whitelist'])
        b_generateNewKeys = bool(self.config['DEFAULT']['GenerateNewKeys']) # Not a self.arrtibute - only needed temporarily
        
        self.whitelist = []

        # generate new keys if stated in the config.conf file
        if b_generateNewKeys:
            generate_keys.generateNewKeys(self.d_PubKey, self.d_PrivKey)
        # load keys from the public.pem and private.pem files
        self.PubKey, self.PrivKey = load_keys.loadKeys(self.d_PubKey, self.d_PrivKey)

        if self.b_Whitelist:
            try:
                self.whitelist = read_whitelist.readWhitelist(self.d_Config)
            except:
                raise IndexError("Whitelist Error: could not retrieve whitelist")
        

        self.context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        self.context.load_cert_chain(self.d_PubKey, self.d_PrivKey)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        print(f"Server now listening on port {self.port}")


    def accpet_connection(self):
        new_socket, fromaddr = self.socket.accept()

        if self.b_Whitelist:
            pass

        

    
    
        

