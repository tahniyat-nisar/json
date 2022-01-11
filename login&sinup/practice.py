

def password(pswrd):
   import re
   if len(pswrd)>=6 and len(pswrd)<=16:
      if re.findall("[a-z]", pswrd):
         if re.findall("[A-Z]", pswrd):
            if re.findall("[0-9]", pswrd):
               if ("@" or "#")in pswrd:
                  print(pswrd, "is a strong password")
               else:
                  print("it does not have any special character")
                  pswrd=input("enter 8 characters strong password:")
                  password(pswrd)
                  
            else:
               print("it does not have any digit")
               pswrd=input("enter 8 characters strong password:")
               password(pswrd)
               
         else:
            print("it does'nt have any uppercase")
            pswrd=input("enter 8 characters strong password:")
            password(pswrd)
      else:
         print("it does'nt have any lowercase")
         pswrd=input("enter 8 characters strong password:")
         password(pswrd)
         
   else:
      print("it's length should be between 6 and 16")
      pswrd=input("enter 8 characters strong password:")
      password(pswrd)
      
def function_username(user_name):
   import re
   if re.findall("[a-zA-Z]",user_name):
      print(user_name)
   else:
      print("invalid format")














   # 
   # if len(pswrd)>=6 or len(pswrd)<=16:
   #    if pswrd>="a" or pswrd<="z":
   #       if pswrd>="A" or pswrd<="Z":
   #          if pswrd>="0" or pswrd<="9":
   #             if ("@" or "#") in pswrd:
   #                print("it is a strong password")
   #             else:
   #                print("it does not have special character")
   #                pswrd3=input("enter 8 characters password:")
   #                password(pswrd3)
   #          else:
   #             print("it does not have any number")
   #             pswrd3=input("enter 8 characters password:")
   #             password(pswrd3)
   #       else:
   #          print("it does not have uppercase letter")
   #          pswrd3=input("enter 8 characters password:")
   #          password(pswrd3)
   #    else:
   #       print("it does not have any lowercase letter")
   #       pswrd3=input("enter 8 characters password:")
   #       password(pswrd3)
   # else:
   #    print("password length is short")
   #    pswrd3=input("enter 8 characters password:")
   #    password(pswrd3)
      

# def function_username(user_name):
#    if user_name>="A" or user_name<="Z":
#       if user_name>="a" or user_name<="z":
#          return user_name
#       else:
#          print("enter user name in correct format")
#          user_name=input("enter the user name:")


# def function_confirm_pswrd():
#    pswrd1=password()
#    print("renter your password to get confirmed")
#    pswrd2=password()
#    print("checking...")
#    if pswrd1 == pswrd2:
#       return pswrd2
#       print("wait for a moment\nto get login")
#    else:
#       print("both paswords are not same")
#       function_confirm_pswrd()

def function_signup():
   user_name=input("enter a user name:")
   function_username(user_name)

   description=input("write a description about you:")
   def DOB():
      Date=int(input("enter your Birth Date:"))
      if Date>=1 and Date<=31:
         month=input("enter your Birth Month Name(like for ex:Jan):")
         if month in ("Jan","Feb","March","Apr","May","Jun","July","Aug","Sep","Oct","Nov","Dec"):
            year=int(input("enter your Birth Year:"))
            if year>=1000 or year<=3000:
               print("your DOB is",Date,month,year)
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

   Q_lis=["user Name","Description","Birth Date","Hobbies","Gender"]
   temp_tuple=(user_name,description,Birth_date,hobbies,Gender)
   A_lis=list(temp_tuple)
   test_dict={}
   for index in range(len(Q_lis)):
      test_dict[Q_lis[index]]=A_lis[index]
   # print(test_dict)


print("WELCOME TO FACEBOOK")
Input=input("choose option\n1.signup\n2.login\n")
if Input=="1":
   print("WELCOME TO FACEBOOK SIGNUP PAGE")
   print("Let's create a new account")
   function_signup()
   print("Let's create a new password\ncontaining combination of numbers,capital letters,small letters,special characters")
   pswrd=input("enter 8 characters strong password:")
   print(password(pswrd))
   print("congrats,you have sucessfully created a facebook account")
   print("now your redirected to login page\n to signin to your account")
elif Input=="2":
   print("WELCOME TO LOGIN PAGE OF FACEBOOK")
   user_name=input("enter username:")
   function_username(user_name)
   pswrd=input("enter 8 characters strong password:")
   password(pswrd)
   re_pswrd=input("renter your password to confirm:")
   if re_pswrd==pswrd:
      Login_Dict={"USER_NAME":user_name,"PASSWORD":re_pswrd}
      print(Login_Dict)
   else:
      print("your password does'nt match")



