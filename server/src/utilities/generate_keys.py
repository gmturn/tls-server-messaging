import rsa

def generate_new_keys(d_PubKey, d_PrivKey): # pass in the file location for public and private key path
    pubKey, privKey = rsa.newkeys(1024)
    
    # writing keys to their respective files
    with open(d_PubKey, "wb") as f:
        f.write(pubKey.save_pkcs1("PEM"))
    with open(d_PrivKey, "wb") as f:
        f.write(privKey.save_pkcs1("PEM"))
    