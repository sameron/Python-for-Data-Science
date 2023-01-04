# Python program to perform CRUD operations on a dictionary

# create a dictionary
d = {
    "name": "John Smith",
    "age": 30,
    "city": "New York"
}

# print the dictionary
print(d)

# read a value from the dictionary
print(d["name"])

# update a value in the dictionary
d["age"] = 35

# print the updated dictionary
print(d)

# delete a key-value pair from the dictionary
del d["age"]

# print the modified dictionary
print(d)
