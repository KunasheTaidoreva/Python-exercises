def screen_menu():
        print("MAIN MENU...")
        print("1. Start Game")
        print("2. Exit Game")
        print("3. View Player Info")
        print("4. lopeta")
        selection  = str(input("Enter number between 1 and 4 : "))
        while selection != "4":
            #assigning different commands to different responses then outputting the main menu again
            if selection == "1":
                print("Starting the game...")
                start_game()
                selection  = str(input("Enter number between 1 and 4 :"))
            elif selection == "2":
                print("Ending the game, see you soon!...")
                break
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

def team_route():

    global items

    print("You decided to work with the other prisoners.")
    print("Together, you make a plan to escape.")

    print("You have one job:")
    print("1. Watch for the guards and find the key if spotted")

    choice = input("Enter one to proceed: ")

    if choice == "1":
        print("You watch the hallway.")
        print("A guard is coming!")
        print("You and your group now have to figure out the key code for the door.")

        print(f"The security code has 3 places: {items}")

        # Question 1
        attempts = 0

        while attempts < 2:
            m1 = float(input("What is the square root of 64? "))

            if m1 == 8:
                items.append(m1)
                print(f"Your passcode is taking shape: {items}")
                break
            else:
                print("Try again.")
                attempts += 1

        if attempts == 2:
            print("You failed to crack the first part of the code.")
            screen_menu()
            return

        # Question 2
        attempts = 0

        while attempts < 2:
            print("Okay, moving to the next question.")

            m2 = int(input("A leap year is a year divisible by ___? "))

            if m2 == 4:
                items.append(m2)
                print(f"You're one step closer to cracking that code: {items}")
                break
            else:
                print("Don't quit now. Give it another shot.")
                attempts += 1

        if attempts == 2:
            print("You failed to crack the second part of the code.")
            screen_menu()
            return

        # Question 3
        attempts = 0

        while attempts < 2:
            print("Last question.")

            m3 = int(input("How many hours does an average human need to rest? "))

            if m3 == 8:
                items.append(m3)
                print("You really know what you are doing! :)")
                print(f"Here is your passcode: {items}")
                print("You have cleared this stage!")
                break
            else:
                print("You're almost there. DO NOT GIVE UP NOW!!!")
                attempts += 1

        if attempts == 2:
            print("You failed to crack the final part of the code.")
            screen_menu()
            return

        # Successful team route stage
        print("\nThe security door unlocks!")
        print("Your group quietly moves forward...")

    else:
        print("Invalid choice.")
        screen_menu()

def Lone_wolf():
    import random
    print("You're now on your own!!!")
    print("Keep in mind you've got 3 chances for this stage")
    x = random.randint(1,25)
    y = random.randint(26,50)
    count = 0
    flag = False
    while count<3:
        rNum = int(input("Enter a random number between 1 and 50: "))
        if rNum >= x and rNum <= y:
            print("Congratulations you guessed correct!!!")
            flag = True
            break
        else:               
            count+=1        
    if flag == True:
        print("You got lucky, guard didn't spot you")
        print("Moving on to the next level")
    else:
        print("You've been spotted by a guard. RUNNN!!!")
        Escaping_Guard()        