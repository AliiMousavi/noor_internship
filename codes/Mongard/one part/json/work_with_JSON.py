"""
json -> dump, dumps, load, loads
"""

import json

with open("my.json") as f:
    data = json.load(f)

print(data)
del data['age']

print(data)

with open("my2.json", "w") as d:
    json.dump(data, d)