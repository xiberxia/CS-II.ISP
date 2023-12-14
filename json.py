# json tutorial @ https://www.w3schools.com/python/python_json.asp

import json

#--------------------------------------------------------#

# PARSING JSON TO PYTHON
# ex. JSON
x = '{"q1": "a1", "q2": "a2", "q3": "a3"}

# parse x
y = json.loads(x)

#results in python dictionary:
print(y["q1"])

#--------------------------------------------------------#

# PYTHON TO JSON
# ex. python dictionary
x = {
  "q1": "a1"
  "q2": "a2"
  "q3": "a3"
}

# convert into JSON
y = json.dumps(x)

# results in JSON string:
print(y)

#--------------------------------------------------------#
