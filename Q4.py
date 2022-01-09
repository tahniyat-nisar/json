# Q4.Python dictionary(sort by key) object ko json data ::
# mai convert karne ka program likho?

py_obj={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}

import json
json_data=json.dumps(py_obj,sort_keys=True)
print(json_data)