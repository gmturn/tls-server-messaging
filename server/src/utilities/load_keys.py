import rsa

def load_keys(d_PubKey, d_PrivKey):
    with open(d_PubKey, "rb") as f:
        pubKey = rsa.PublicKey.load_pkcs1(f.read())
    
    with open(d_PrivKey, "rb") as f:
        privKey = rsa.PrivateKey.load_pkcs1(f.read())

    return pubKey, privKey