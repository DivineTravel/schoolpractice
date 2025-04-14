username = input("Enter username: ")
if username == "admin":
    password = input("Enter password: ")
    if password == "1234":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("This user does not exist")
