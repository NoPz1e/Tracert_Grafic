import sys, os
import requests
import json

# Sends an HTTP GET request to API
# retrieves the Response
# decodes it
# converts into python library object
def retrieveCoordinates(ip):
    req = requests.get(f"http://ip-api.com/json/{ip}?fields=status,lat,lon")
    content = json.loads(req.content.decode())  
    if content["status"] == "success":
        return {"lat": content["lat"], "lon": content["lon"]}
    else:
        return None


# print(retrieveCoordinates("192.168.1.1"))