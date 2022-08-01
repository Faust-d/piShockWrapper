import requests

class piShock:
    username: str = None
    apikey: str = None
    code: str = None
    name: str = None
    def __init__(self, username, apikey, code, name):
        if username == None or apikey == None or code == None or name == None:
            """Missing required parameters"""
        elif name == "PiShock":
            """'name' must be different from PiShock"""
        else:
            session = requests.Session()

