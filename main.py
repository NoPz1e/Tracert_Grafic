import sys, os
import ast
import ui

if not os.path.exists("log.txt"):
    print("Log file does not exist.")
    sys.exit()
else:
    try:
        file = open("log.txt", "r")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit()

routeLog = []
for line in file:
    routeLog.append(line)

for entry in routeLog[1:]:
    node = ast.literal_eval(entry)
    print(node["ip"])