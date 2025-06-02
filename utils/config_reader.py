import configparser
import os

def read_config(section, key):
    config = configparser.ConfigParser()
    config.read('config.ini') # Ou outro arquivo de configuração
    return config.get(section, key)

def get_env_variable(var_name):
    return os.environ.get(var_name)