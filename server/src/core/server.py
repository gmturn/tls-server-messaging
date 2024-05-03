#import server.src.utilities.config_loader as conf
from server.src.utilities import generate_keys, load_keys, read_whitelist
import server.src.utilities.config_loader as conf
from server.src.handlers.request_handler import RequestHandler


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
        self.d_CertFile = str(self.config['DEFAULT']['CertificatePath'])
        self.d_PrivKey = str(self.config['DEFAULT']['PrivateKeyPath'])

        self.d_Log = self.config['DEFAULT']['LogPath']
        self.logging = self.config['DEFAULT']['Logging']
        self.b_Whitelist = bool(self.config['DEFAULT']['Whitelist'])
        
        self.whitelist = []

       
        # load keys from the public.pem and private.pem files
        # self.PubKey, self.PrivKey = load_keys.loadKeys(self.d_PubKey, self.d_PrivKey)

        if self.b_Whitelist:
            try:
                self.whitelist = read_whitelist.readWhitelist(self.d_Config)
            except:
                raise IndexError("Whitelist Error: could not retrieve whitelist")
        

        # self.context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        # self.context.load_cert_chain('server/keys/cert.pem', 'server/keys/key.pem')
        # self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)



        self.socket = socket.socket()
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        
        print(f"Server now listening on port {self.port}")


    def accept_connection(self):
        while True:
            newsocket, fromaddr = self.socket.accept() # (awaits connection)
            

            # creating a secure connection
            try:
                secure_socket = ssl.wrap_socket(newsocket,
                                            server_side=True,
                                            certfile=self.d_CertFile,
                                            keyfile=self.d_PrivKey,
                                            ssl_version=ssl.PROTOCOL_TLSv1,
                                            do_handshake_on_connect=True)
            except:
                print("Error: Could not establish secure connection with client. Exiting")
                
            # Verifying connection permission from whitelist
            if self.b_Whitelist:
                try:
                    fromaddr in self.whitelist
                except:
                    raise PermissionError(f"Error: IP Address [{fromaddr}] not whitelisted")

            request_handler = RequestHandler(secure_socket, fromaddr)
            request_handler.handle_request()



        

    
    
        

