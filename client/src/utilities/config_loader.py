import configparser

# load contents of the config file
# return configparser instance
def load_config(config_path):
    config = configparser.ConfigParser()
    config.read(config_path + "config.conf")
    return config