# Q7.Text file data ko json file data mai convert karo,
# jaise ki neeche diya hai?

# file=open("Text.txt","x")
# file.write("""Name Abhishek
# Designation CEO of navgurukul
# Gender male
# Age 29""")
# file.close()



file=open("Text.txt","r")
data=file.read()
print(data.strip("\n"))

import json
with open('TXT.json', 'w') as json_file:
  json.dump(data.strip("\n"), json_file,indent=4)





# import json

# meraki_dict = {"Name": "Abhishek",
# "Designation":"CEO of navgurukul",
# "Gender": "male",
# "Age" :29
# }

# with open('meraki.txt', 'w') as json_file:
#   json.dump(meraki_dict, json_file,indent=4,sort_keys=True)







