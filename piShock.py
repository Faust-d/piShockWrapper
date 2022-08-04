import requests
import time


class piShock:
    """
    piShock methods: shock, vibe, beep

    Shock: piShock.shock(username, apikey, code, name, duration, intensity, <Optional>warning)
    Vibe: piShock.vibe(username, apikey, code, name, duration, intensity)
    Beep: piShock.beep(username, apikey, code, name, duration)
    """
    def __init__(self, username:str, apikey:str, code:str, name:str, duration:int=0, intensity:int=0, warning:int=0):
        if username == None or apikey == None or code == None or name == None or intensity == None or duration == None:
            """Missing required parameters"""
        elif name == "PiShock":
            """'name' must be different from PiShock"""
        elif duration > 15 or duration < 1:
            """Duration must be between 1 and 15"""
        elif intensity > 100 or intensity < 1:
            """Intensity must be between 1 and 100"""

    def shock(username:str, apikey:str, code:str, name:str, duration:int, intensity:int,  warning:int=0):
        """
        Shock the device for a duration of time, with warning if desired.
        Requires Username, API Key, Share Code, a name for the API call, duration between 1-15, and intensity between 1-100.
        You can also include a warning, in a duration of seconds between the shock and the warning.

        Use: piShock.shock(username, apikey, code, name, duration, intensity, <<Optional>warning)
        """
        operation = 0
        if warning > 0:
            do(username, apikey, code, name, 1, 1, intensity)
            time.sleep(warning)
        return do(username, apikey, code, name, operation, duration, intensity)

    def vibe(username:str, apikey:str, code:str, name:str, duration:int, intensity:int):
        """
        Vibe the device for a duration of time.
        Requires Username, API Key, Share Code, a name for the API call, duration between 1-15, and intensity between 1-100.

        Use: piShock.vibe(username, apikey, code, name, duration, intensity)
        """
        operation = 1
        return do(username, apikey, code, name, operation, duration, intensity)

    def beep(username:str, apikey:str, code:str, name:str, duration:int):
        """
        Beep the device for a duration of time.
        Requires Username, API Key, Share Code, a name for the API call, duration between 1-15.
        
        Use: piShock.beep(username, apikey, code, name, duration)
        """
        operation = 2
        return do(username, apikey, code, name, operation, duration)

        
#Submit api request.
def do(username, apikey, code, name, operation, duration, intensity=0):
    """
    Submit api request.
    """
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