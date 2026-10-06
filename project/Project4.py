#importing the Project3.py file to Project4.py file as a module to use its functions in this file.
import Project3

class Verification:
    def __init__(self,Name,Age):
        self.Name = Name
        self.Age = Age
    def verify_age(self):
        if self.Age <= 12:
            print("Sorry, you are underage!!!")
            print("SHUTTING DOWN THE GAME....!!!")
        else:
            print("Hello", self.Name)
            selection = ""
            while selection != "3":
                print("\nMAIN MENU...")
                print("1. Start Game")
                print("2. View Player Info")
                print("3. Exit Game")
                selection = input("Enter number between 1 and 3: ")
                if selection == "1":
                    a = self.Name
                    b = self.Age
                    Project3.start_game(a,b)
                elif selection =="2":
                    print(f"PLAYER ID: {self.Name}")
                    print(f"PLAYER AGE: {self.Age}")
                elif selection == "3":
                    print("Ending the game, see you soon!...")
                else:
                    print("Invalid selection.")

 