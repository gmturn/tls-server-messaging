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



        self.context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        self.context.load_cert_chain(certfile=self.d_CertFile, keyfile=self.d_PrivKey)
        
        self.s_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s_Socket.bind((self.host, self.port))
        self.s_Socket.listen(5)
      
        print(f"Server now listening on Port[{self.port}]")


    def accept_connection(self):
        while True:
            newsocket, address = self.s_Socket.accept()
            # whitelist check
            try:
                address in self.whitelist
            except:
                raise PermissionError(f"Error: IP {address} not in whitelist. Exiting.")
            
            
            try:
                secure_socket = self.context.wrap_socket(newsocket, server_side=True)
                print(f"Secure connection with IP [{address}] established...")
                
                data = secure_socket.read()
                while data:
                    print(data)
                    response = str(input("Response: "))
                    secure_socket.sendall(response.encode())
                    data = secure_socket.read()
                
                print(f"Secure connection with IP [{address}] terminated.")
                secure_socket.close()

            

            except ssl.SSLError as e:
                print(f"SSL error: {e}")
            except Exception as e:
                print(f"Error: could not establish connection with clinet: {e}")
            


        
        # creating a secure connection
        try:
            pass
        except:
            connection, address = self.secure_socket.accept()
            
       


        

    
    
        

