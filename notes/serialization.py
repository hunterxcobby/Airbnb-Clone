#!/usr/bin/python3

import json

"""serialize the data"""

data = {
    "name" : "Cobby",
    "age" : 22,
    "course": ["Maths", "Science", "Computer Science"]
}

# convert to json formatted string
# json_string = json.dumps(data, indent=4)

# save to a file
with open("data.json", "a") as json_file:
    json_file = json.dump(data, json_file, indent=4)


