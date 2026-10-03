#importing the Project4.py file to Project5.py file as a module to use its functions in this file.
import Project4
with open("project/GameIntro.txt","r") as file:
    data = file.read()
    print(data)
Name = str(input("Enter your player name: "))
Age = int(input("Enter your age: "))

Player = Project4.Verification(Name,Age)
Player.verify_age()
