# Q8.Tumhare pass four employes ki details hai list mai:-

# ab aapko 4 dictionaries create karni hai jaise ki emp1 emp2 emp3 and emp4.
# har ek employee ka dictionary main name,designation,age and salary honi chahiye.
# aur ye sab dictionary ki keys hai jismai maine list main value di 
# hai. Iska use kar ke aapko ek json file create karni hai? Jaise ki niche diya hai.



lis=[['neelam','programer','24','2400',],
['komal','trainer','24','20000'],
["anuradha",'HR','25','40000'],
['Abhishek','manager','29','63000']]

i=0
temp_lis=[]
while i<len(lis):
   dic=(dict(name=lis[i][0],designation=lis[i][1],
   age=lis[i][2],salary=lis[i][3]))
   temp_lis.append(dic)
   i=i+1
print(temp_lis)

employees_list=['emp1','emp2','emp3','emp4']
Dict={}
for i in range(len(temp_lis)):
   Dict[employees_list[i]]=temp_lis[i]
print(Dict)

import json
with open("employees_details.json","w") as emp_json_file:
   json.dump(Dict,emp_json_file,indent=4)




