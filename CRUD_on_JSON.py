# Python program that performs CRUD operations on a JSON object

import json

# create a JSON object
json_obj = {
    "name": "John Smith",
    "age": 30,
    "city": "New York"
}

# convert the JSON object to a string
json_str = json.dumps(json_obj)

# print the JSON string
print(json_str)

# convert the JSON string back to an object
obj = json.loads(json_str)

# print the object
print(obj)

# update the object
obj["age"] = 35
obj["city"] = "Los Angeles"

# convert the updated object back to a string
json_str = json.dumps(obj)

# print the updated JSON string
print(json_str)

# delete a key-value pair from the object
del obj["age"]

# convert the modified object back to a string
json_str = json.dumps(obj)

# print the modified JSON string
print(json_str)
