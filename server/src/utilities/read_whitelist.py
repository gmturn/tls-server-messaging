# load contents of whitelist file
# return list of whitelisted IP addresses
def readWhitelist(configPath):
    d_Whitelist = configPath + "whitelist.txt"
    whitelist = []
    with open(d_Whitelist, 'r') as f:
        whitelist = f.read().splitlines()
    return whitelist