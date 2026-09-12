Name = str(input("Enter your player name: "))
Age = int(input("Enter your age: "))

items = []
# Function for starting the game
def start_game():
    print("Starting the game...")


# Function for adding an item to the list
def add_item():
    item = input("Enter an item: ")
    items.append(item)
    print("Item added!")


# Function for displaying the items
def view_items():
    print("Your items:")
    
    if len(items) == 0:
        print("The list is empty.")
    else:
        for item in items:
            print(item)


# Function for viewing player information
def view_player_info():
    print("Player name =", Name)
    print("Age =", Age)


# Checking if the player is underage
if Age <= 12:
    print("Sorry, you are underage!!!")
    print("SHUTTING DOWN THE GAME....!!!")
else:
    print("Hello", Name)
    selection = ""
    while selection != "5":
        print("\nMAIN MENU...")
        print("1. Start Game")
        print("2. Add Item")
        print("3. View Items")
        print("4. View Player Info")
        print("5. Exit Game")
        selection = input("Enter number between 1 and 5: ")
        if selection == "1":
            start_game()
        elif selection == "2":
            add_item()
        elif selection == "3":
            view_items()
        elif selection == "4":
            view_player_info()
        elif selection == "5":
            print("Ending the game, see you soon!...")
        else:
            print("Invalid selection.")

    print("No more commands")