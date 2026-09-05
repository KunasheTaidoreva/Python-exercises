Name = str(input("Enter your player name: "))
Age = int(input("Enter your age: "))

#Checking if the player is underage or eligible to continue
if Age <= 12:
    print("Sorry, you are underage!!!")
    print("SHUTTING DOWN THE GAME....!!!")
else:
    print("Hello", Name)
    #printing the main menu of the game
    print("MAIN MENU...")
    print("1. Start Game")
    print("2. Exit Game")
    print("3. View Player Info")
    print("4. lopeta")
    selection  = str(input("Enter number between 1 and 4 "))
    while selection != "4":
        #assigning different commands to different responses then outputting the main menu again
        if selection == "1":
            print("Starting the game...")
            print("MAIN MENU...")
            print("1. Start Game")
            print("2. Exit Game")
            print("3. View Player Info")
            print("4. lopeta")
            selection  = str(input("Enter number between 1 and 4 :"))
        elif selection == "2":
            print("Ending the game, see you soon!...")
            print("MAIN MENU...")
            print("1. Start Game")
            print("2. Exit Game")
            print("3. View Player Info")
            print("4. lopeta")
            selection  = str(input("Enter number between 1 and 4 :"))
        elif selection == "3":
            print("Player name =", Name)
            print("Age =", Age)
            print("MAIN MENU...")
            print("1. Start Game")
            print("2. Exit Game")
            print("3. View Player Info")
            print("4. lopeta")
            selection  = str(input("Enter number between 1 and 4 :"))
        print("No more commands")