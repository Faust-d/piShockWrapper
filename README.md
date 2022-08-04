# piShock API Wrapper
This is a simple wrapper for the piShock, and soon the piVault as well.

Please read the piShock safety disclaimers before using, I am not liable for what you do with my script.

# Setup
* Install Python 3
* Open a terminal/command prompt and run `pip install requests`

# Use
You can import piShock or piVault API wrappers seperately, simply by including 
* `from piShockWrapper import piShock`
* `from piShockWrapper import piVault`

# piShock
* `username`, string, your piShock username
* `apikey`, string, your piShock API key.
* `sharecode`, string, the share code of the shocker you want to control.
* `name`, string for the name that will be showned in logs IE: `piShock API Example`
* `duration`, integer between 1 and 15.
* `intensity`, integer between 1 and 100.
* `warning`, *optional* integer between 1 and 10, will only be used if it is assigned.
  - Warning will vibe for 1 second at the specified intensity, and wait for the duration specified before sending a shock.

There are three methods included with the piShock API Wrapper.
* Shock `piShock.shock`
  - `piShock.shock(username, apikey, sharecode, name, duration, intensity, <Optional>warning)`
* Vibrate `piShock.vibe`
  - `piShock.vibe(username, apikey, code, name, duration, intensity)`
* Beep `piShock.beep`
  - `piShock.beep(username, apikey, code, name, duration)`

The API will return a result as a list.
* `[httpcode, 'result string']`
  - IE: `[200, 'Operation Succeeded.']`
Please refer to the API documentation for a list of status codes and responses.

# piVault
Currently piVault functionality is unimplimented, but will be worked on as soon as possible.