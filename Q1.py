# Q.1 Json data ko python object main 
# convert karne ka program likho?.


import json
data={"language":["python","javascript"],"girls":250,7:45}
json_data=json.dumps(data)
print(type(data))
print(data)
print(type(json_data))
print(json_data)



python_obj=json.loads(json_data)
print(python_obj)
print(type(python_obj))