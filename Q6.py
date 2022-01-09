# Q6.Python object ki unique key values nikalo 
# par vo unique values json object or json data me ani chahiye?

python_obj={
 "a":  1,
 "a":  2,
 "a":  3, 
 "a": 4,   
 "b": 1, 
 "b": 2}
print(python_obj)

import json
json_obj=json.dumps(python_obj)
print(json_obj)