name = "python"
security_code = "rules"
# username as string
# #password as integer
username = str(input("Enter your username: "))
password = str(input("Enter your password: "))
#count as variable storing the number of authorisation attempts
count = 0
while count <=5:
    if username == name and password == security_code:
        print("Welcome!!")
        break
    else:
        print("Invalid username or password. Please try again.")
        count = count + 1
        if count< 5:
            username= str(input("Username: "))
            password = str(input("Password: "))
if count == 5 and (username != name or password != security_code):
    print("Access denied.")