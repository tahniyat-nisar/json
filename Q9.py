python_obj={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
import json
with open("shopping_list.json","w") as json_file:
   json.dump(python_obj, json_file,indent=4)



with open("shopping_list.json","r") as json_file:
   shopping_list_py=json.load(json_file)
Dic={}
lis=[]
for main_value in shopping_list_py.values():
        for keys,values in main_value.items():
            lis.append(keys)
while True:        
    for main_value in shopping_list_py.values():
        for keys,values in main_value.items():
            pass
    select_item=input("Kounsa Item Khareed Na Chahte Hoo:")
    if select_item in lis:
        print("Arrey Yeh Toh Hamare Shopping List Me Phele Se Hai")
        print("dekho\n",lis)
        print(shopping_list_py)
        for k,v in main_value.items():
            if select_item==k:
                print("Accha Inki Ginti Mai Koi Changes Karna chahte ho kya?")
                No_of_items=int(input("kitney kareed na chahte ho ye wala item:"))
                v=int(v)
                if No_of_items>v:
                    v=No_of_items-v
                    Dic.update({select_item:str(v)})
                elif No_of_items<v:
                    v=v-No_of_items
                    Dic.update({select_item:str(v)})
                else:
                    Dic.update({select_item:str(v)})
    else:
        print("ab samaj aya apko kuch naye items chahiye\njo iss list me nahi hai")
        No_of_items=int(input("kitney kareed na chahte ho:"))
        Dic.update({select_item:str(No_of_items)})      
    print(Dic)
    with open("shopping_list.json","w") as json_file:
        json.dump(Dic, json_file)


import json

































