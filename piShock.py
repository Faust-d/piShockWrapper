import requests
import json

class piShock:
    username: str = None
    apikey: str = None
    code: str = None
    name: str = None
    operation: str = None
    intensity: int = None
    duration: int = None
    def __init__(self):
        pass
    def __new__(self, username, apikey, code, name, operation, intensity, duration):
        if username == None or apikey == None or code == None or name == None or operation == None or intensity == None or duration == None:
            """Missing required parameters"""
        elif name == "PiShock":
            """'name' must be different from PiShock"""
        elif duration > 10 or duration < 1:
            """Duration must be between 1 and 10"""
        elif intensity > 100 or intensity < 1:
            """Intensity must be between 1 and 100"""
        else:
            session = requests.Session()
            session.params = {}
            session.params['Username'] = username
            session.params['Name'] = name
            session.params['Code'] = code
            session.params['Intensity'] = intensity
            session.params['Duration'] = duration
            session.params['Apikey'] = apikey
            session.params['Op'] = operation
            response = session.post('https://do.pishock.com/api/apioperate', json=session.params)
            return [response.status_code, response.text]