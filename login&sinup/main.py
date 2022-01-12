
def password(pswrd):
   import re
   flag = True
   while flag==True:
      if len(pswrd)>=6 and len(pswrd)<=16:
         if re.findall("[a-z]", pswrd):
            if re.findall("[A-Z]", pswrd):
               if re.findall("[0-9]", pswrd):
                  if ("@" or "#")in pswrd:
                     print(pswrd, "is a strong password")
                     return pswrd
                     flag=False
                     break
                  else:
                     print("it does not have any special character")
                     pswrd=input("enter 8 characters strong password:")
                     # password(pswrd)
                     
               else:
                  print("it does not have any digit")
                  pswrd=input("enter 8 characters strong password:")
                  # password(pswrd)
                  
            else:
               print("it does'nt have any uppercase")
               pswrd=input("enter 8 characters strong password:")
               # password(pswrd)
         else:
            print("it does'nt have any lowercase")
            pswrd=input("enter 8 characters strong password:")
            # password(pswrd)
            
      else:
         print("it's length should be between 6 and 16")
         pswrd=input("enter 8 characters strong password:")
         # password(pswrd)
         
def function_username(user_name):
   import re
   if re.findall("[a-zA-Z]",user_name):
      print(user_name)
   else:
      print("invalid format")

def function_signup():
   user_name=input("enter a user name:")
   function_username(user_name)
   print("Let's create a new password\ncontaining combination of numbers,capital letters,small letters,special characters")
   def confirm_pswrd():
      pswrd=input("enter 8 characters strong password:")
      x=password(pswrd)
      re_pswrd=input("renter your password to confirm:")
      if re_pswrd==x:
         return re_pswrd
         print("your new password is created")
      else:
         print("your password does'nt match")
         flag=True
         while flag==True:
            repw=input("Please re-enter the correct password")
            if pswrd==repw:
               print("your new password is created")
               return repw
               break
   PASSWORD=confirm_pswrd()
   description=input("write a description about you:")
   def DOB():
      Date=int(input("enter your Birth Date:"))
      if Date>=1 and Date<=31:
         month=input("enter your Birth Month Name(like for ex:Jan):")
         if month in ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"):
            year=int(input("enter your Birth Year:"))
            if year>=1000 or year<=3000:
               return(Date,month,year)
         else:
            print("please enter the month in correct format")
            DOB()
      else:
         print("please enter the correct date\nfor example btw (1-31)")
         DOB()
   Birth_date=DOB()
   hobbies=input("write your hobbies\nfor example:playing valleyball\n")
   def gender():
      gender=int(input("enter your gender:\n1.male\n2.female\n3.others\n"))
      if gender==1:
         return "male"
      elif gender==2:
         return "female"
      elif gender==3:
         return "others"
      else:
         print("please give correct input")
         return gender()
   Gender=gender()
   print("")

   Q_lis=["user Name","password","Description","Birth Date","Hobbies","Gender"]
   temp_tuple=(user_name,PASSWORD,description,Birth_date,hobbies,Gender)
   A_lis=list(temp_tuple)
   test_dict={}
   for index in range(len(Q_lis)):
      test_dict[Q_lis[index]]=A_lis[index]
   # print(test_dict)
   import json
   import os.path
   if os.path.exists("/home/bharati/Desktop/login or signup/userdetails.json")==True:
      with open("userdetails.json","r") as json_file:
         data=json_file.read()
         previous=json.loads(data)
         previous.append(test_dict)
      with open("userdetails.json","w") as json_file:
         json.dump(previous,json_file,indent=4)
   else:
      with open("userdetails.json","w") as json_file:
         json.dump([test_dict],json_file,indent=4)
   


print("WELCOME TO FACEBOOK")
Input=input("choose option\n1.signup\n2.login\n")
if Input=="1":
   print("WELCOME TO FACEBOOK SIGNUP PAGE")
   print("Let's create a new account")
   function_signup()
   print("congrats,you have sucessfully created a facebook account")
   print("now your redirected to login page\nto signin to your account")
elif Input=="2":
   print("WELCOME TO LOGIN PAGE OF FACEBOOK")
   user_name=input("enter username:")
   function_username(user_name)
   pswrd=input("enter 8 characters strong password:")
   password(pswrd)
   Login_Dict={"USER_NAME":user_name,"PASSWORD":pswrd}
      # print(Login_Dict)
   import json
   import os.path
   if os.path.exists("/home/bharati/Desktop/login or signup/userdetails.json")==True:
      with open("userdetails.json","r") as json_file:
         data=json_file.read()
         previous=json.loads(data)
         if (user_name and pswrd) in data:
            print("congrats,your are succesfully logged in")
         else:
            print("your account does'nt exist\ncreate new account by signup")
            function_signup()
   else:
      print("your account does'nt exists\ncreate new account by signup")
      function_signup()








   






