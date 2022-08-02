import requests
import time
username = ''
apikey = ''
code = ''
name = ''
duration = 0
operation = 0
intensity = 0

class piShock:
    def __init__(self, username, apikey, code, name, intensity, duration):
        if username == None or apikey == None or code == None or name == None or intensity == None or duration == None:
            """Missing required parameters"""
        elif name == "PiShock":
            """'name' must be different from PiShock"""
        elif duration > 15 or duration < 1:
            """Duration must be between 1 and 15"""
        elif intensity > 100 or intensity < 1:
            """Intensity must be between 1 and 100"""
    def shock(username, apikey, code, name, intensity, duration, warning=0):
        operation = "0"
        if warning > 0:
            do(username, apikey, code, name, 1, intensity, 1)
            time.sleep(duration+1)
        return do(username, apikey, code, name, operation, intensity, duration)

    def vibe(username, apikey, code, name, intensity, duration):
        operation = "1"

        return do(username, apikey, code, name, operation, intensity, duration)

    def beep(username, apikey, code, name, duration):
        operation = "2"

        return do(username, apikey, code, name, operation, intensity, duration)

        



#Submit api request.
async def do(username, apikey, code, name, operation, intensity, duration):
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