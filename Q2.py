# Q.2 Python object ko json data main convert 
# karne ka program likho?


python={
    "name": "David", 
    "class": "I", 
    "age": 6
}

print(python)
print(type(python))



import json
json_data=json.dumps(python)

print(json_data)
print(type(json_data))
