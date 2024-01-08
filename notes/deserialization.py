#!/usr/bin/python3

import json

"""deserialize the data"""

# load from the file
with open("data.json", "r") as json_file:
    json_string = json_file.read()

# convert the JSON formatted string to a dictionary
    data = json.loads(json_string)

# use the data as python dictionary 
print(data["name"])
print(data["age"])
print(data["course"])
