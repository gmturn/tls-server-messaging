import server.src.utilities.config_loader as conf

import ssl
import socket

class Client:
    def __init__(self, config_path):
        self.d_Config = config_path
        self.config = conf.load_config(config_path)
        self.port = int(self.config['DEFAULT']['Port'])
        self.host = str(self.config['DEFAULT']['Host'])
        self.d_Cert = str(self.config['DEFAULT']['CertificatePath'])

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.secure_socket = ssl.wrap_socket(self.socket,
                                             ca_certs=self.d_Cert,
                                             cert_reqs=ssl.CERT_REQUIRED,
                                             do_handshake_on_connect=True)
        
    def request_connection(self):
        print(f"Now connecting to {self.host}")
        try:
            self.secure_socket.connect((self.host, self.port))
            self.secure_socket.sendall("")
            print(f"Now connected to IP {self.host}")
        except:
            print("Error connecting. Exiting.")