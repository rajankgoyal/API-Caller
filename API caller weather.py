# Import modules
import network
import urequests

# Connect to WLAN
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("NWRKTEST", "FASTCARS1")
while not wlan.isconnected():
    pass
print('Connected to WLAN')

# Make an API call
response = urequests.get(url='https://api.weather.gov/gridpoints/LWX/77,79/forecast', headers = {'User-Agent': '(goyal.rajan@yahoo.com)'})
data = response.json()
# print(response.text)
print(data['properties']['periods'][0]['temperature'])