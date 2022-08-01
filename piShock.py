class piShock:
    def __init__(self, username, apikey, code, name):
        if username == None or apikey == None or code == None or name == None:
            raise ValueError("Name cannot be empty")
        else:
            pass
