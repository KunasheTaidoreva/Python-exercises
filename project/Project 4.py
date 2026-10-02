import Project3


Name = str(input("Enter your player name: "))
Age = int(input("Enter your age: "))

if Age <= 12:
    print("Sorry, you are underage!!!")
    print("SHUTTING DOWN THE GAME....!!!")
else:
    print("Hello", Name)
    selection = ""
    while selection != "3":
        print("\nMAIN MENU...")
        print("1. Start Game")
        print("2. View Player Info")
        print("3. Exit Game")
        selection = input("Enter number between 1 and 3: ")
        if selection == "1":
            a = Name
            b = Age
            Project3.start_game(a,b)
        elif selection =="2":
            print(f"You are, {Name}, {Age} years old")
        elif selection == "3":
            print("Ending the game, see you soon!...")
        else:
            print("Invalid selection.")

 