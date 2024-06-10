import sys, os
import ast
import ui
import map
import iptoaddr

if not os.path.exists("log.txt"):
    print("Log file does not exist.")
    sys.exit()
else:
    try:
        file = open("log.txt", "r")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit()

strRouteLog = []
libRouteLog = []
coordsList = []
# fill strRouteLog with log of strings
for line in file:
    strRouteLog.append(line)

# convert strings to libs, save in other list
for entry in strRouteLog[1:]:
    libRouteLog.append( ast.literal_eval(entry) )

for log in libRouteLog:
    coordsList.append( iptoaddr.retrieveCoordinates(log["ip"]) )

map.draw_map(libRouteLog, coordsList, strRouteLog[0])