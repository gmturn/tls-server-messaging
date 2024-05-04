import client.src.utilities.config_loader as conf
import client.src.handlers.request_handler as handle

import ssl
import socket

class Client:
    def __init__(self, config_path):
        self.d_Config = config_path
        self.config = conf.load_config(config_path)
        self.port = int(self.config['DEFAULT']['Port'])
        self.host = str(self.config['DEFAULT']['Host'])
        self.d_Cert = str(self.config['DEFAULT']['CertificatePath'])

        # creating context
        self.context = ssl.create_default_context()
        self.context.check_hostname=False
        self.context.verify_mode = ssl.CERT_NONE
        
    def request_connection(self):
        print(f"Now connecting to {self.host}")
        c_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        secure_socket = self.context.wrap_socket(c_Socket, server_hostname=self.host)
        try:
            secure_socket.connect((self.host, self.port))
            #secure_socket.sendall("Hello, all!".encode())
            print(f"Now connected to Host [{self.host}]")
            
            handler = handle.RequestHandler(secure_socket, self.host)
            handler.request_connection()
            
        except Exception as e:
            print(f"Error connecting: {e}. Exiting.")