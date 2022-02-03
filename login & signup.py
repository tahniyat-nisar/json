print("Welcome to FACEBOOK")
print("1.enter your email adress if you already have account to login\n or")
print("2.signup to create new account")
num=int(input("choose your option:"))
if num==1:
   user_name=input("enter your email adress(to login):")
   if '@gmail.com' in user_name:
      print("next")
      pswrd=input("enter your 8 chararcteristics password:")
      print(pswrd)
      if len(pswrd)==8:
         print("proceed")
         if 1 or 2 in pswrd :
            print("ok")
            if ("~!@#$%^&*():{}[]|\<>?/;=-+.'") in pswrd:
               pass
               if ("ABCDEFGHIJKLMNOPQRSTUVWXYZ") in pswrd:
                  pass
                  if ("abcdefghijklmnopqrstuvwxyz") in pswrd:
                     pass
                  else:
                     print("it does'nt have lower case")
               else:
                  print("it does'nt have any upper case")
            else:
               print("it does'nt have any special character")

         else:
            print("it doesn't have any number")
   else:
      print("invalid")
         
   #       else:
   #          print("your password doesn't contain any lowercase letter")
   #    else:
   #       print("your password should be 8 characteristics long ")  
   # else:
   #    print("please enter the valid email adress:")




# elif num==2:
#    Q_lis=["Name","User name","Gender","DOB","Hobbies","BIO","email Id"]
#    A_lis=[]
#    Dict={}
#    for i in range(len(Q_lis)):
#       response=(input(Q_lis[i]+":"))
#       # if Q_lis[i]=="Gender":
#       #    print("1.Male\n2.Female\n3.others")
#       #    print(int(input("select your option:"))
#       A_lis.append(response)
#       Dict[Q_lis[i]]=A_lis[i]
#    print(Dict)
















   # Name=input("enter your name:")
   # User_name=input("enter your user name:")
   # email=input("enter your email ID:")
   # gender=input("enter your gender:")
   # DOB=input("enter your DOB")
   # Hobbies=input("write about your hobbies:")
   # BIO=input("write your short BIO")














# import json
# with open("login.json","w") as login_json_file:
#    json.dump()