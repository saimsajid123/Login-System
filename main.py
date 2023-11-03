
print("Type 1 To Register")
print("Type 2 To Login")
print("Type 3 To Forgot Password")
count = int(input())
 def login():

    if (count==1):
        global reg_user
        reg_user=input("Enter Your Username:")
        global reg_pass
        reg_pass=input("Enter Your Password:")
        return reg_user and reg_pass
    if(count==2):
        username=input("Enter Your Username:")
        password=input("Enter Your Password:")
        if(username==reg_user and password==reg_pass):
            print("You Have Sucessfully Logged In")

        else:
            print("Wrong Password/Username")


login()