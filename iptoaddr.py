import sys, os
import requests
import json

# Sends an HTTP GET request to API
# retrieves the Response
# decodes it
# converts into python library object
def retrieveCoordinates(ip):
    req = requests.get(f"http://ip-api.com/json/{ip}?fields=lat,lon")
    return(json.loads(req.content.decode()))