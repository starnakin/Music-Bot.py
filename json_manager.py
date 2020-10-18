import json

from os import path

config_file_uri="./json/config.json"

if not path.exists(config_file_uri):
    file = open(config_file_uri, 'w')
    json.dump({"token": "", 
                "prefix": "",
                "activity": "",
                "activity_type": ""})
    file.close()
    print("config file has been generate !")

def curent_file(file_uri):
    file=open(file_uri, "r")
    return json.load(file)

def get(file_uri, key):
    file=open(file_uri, "r")
    return json.load(file)[key]