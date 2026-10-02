global Name
global Age
items = []
def game_intro():
    print("*"*15,f"WELCOME TO PRISON ESCAPE GAME", "*"*15)
    print("")
    print("AFTER 15 YEARS IN PRISON, YOU FINALLY GET THE CHANCE TO ESCAPE PRISON THANKS TO THE HEAVY LIGHTNING THAT STRUCK THE MAIN POWER SUPPLY.")
    print("The lighting killed most of the prison's power, leaving the prison vulnerable to escape")
    print("But the doors are now less secure, and you have to make a choice to escape the prison.")


class Game_properties:
    def __init__(self,select,name,age):
        self.select = select
        self.name = name
        self.age = age
    # Function for viewing player information
    def view_player_info(self):
        print("Player name =",self.name)
        print("Age =", self.age)
    # Function for displaying the items
    
    def choice(self):
        if self.select==2:
            self.view_player_info()


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

def Lone_wolf(a,b):
    import random
    print("*"*18,"You're now on your own!!!","*"*18)
    print("Keep in mind you've got 3 chances for this stage")
    x = random.randint(1,25)
    y = random.randint(26,50)
    count = 0
    flag = False
    while count<3:
        print(x,y)
        rNum = int(input("Enter a random number between 1 and 50: "))
        if rNum >= x and rNum <= y:
            print("Congratulations you guessed correct!!!")
            flag = True
            break
        else:               
            count+=1        
    if flag == True:
        print("You got lucky, guard didn't spot you")
    else:
        print("You've been spotted by a guard. RUNNN!!!")
        Escaping_Guard(a)      

def team_route(a,b):
    # list called passcode to hold the players build up passcode
    passcode = []
    print("You decided to work with the other prisoners.")
    print("Together, you make a plan to escape.")
    print("You have one job:")
    print("Watch for the guards and find the key if spotted")
    choice = str(input("Enter 1 to proceed: "))
    if choice == "1":
        print("You watch the hallway.")
        print(" "*20,"!!!A GUARD IS COMING!!!"," "*20)
        print("You and your group now have to find a way to figure out the key code for the door")
        print("The security code has 3 places")

        # QUESTION 1
        c1 = 0
        while c1 < 2:
            m1 = int(input("What is the square root of 64?: "))
            if m1 == 8:
                passcode.append(m1)
                print(f"Your passcode is taking shape:, {passcode}")
                break
            else:
                c1 += 1
                if c1 == 2:
                    print("*"*20,"SORRY,GAME OVER",a,"*"*20)
                    screen_menu(a,b)
                    return
                else:
                    print("You are so close, don't quit now!!!")
       # QUESTION 2
        c2 = 0
        while c2 < 2:
            print("Okay, moving on to the next question")
            m2 = int(input("A leap year is a year divisible by ___?: "))
            if m2 == 4:
                passcode.append(m2)
                print(f"You're one step closer from cracking that code {passcode}")
                break
            else:
                c2 += 1
                if c2 == 2:
                    print("*"*20,"GAME OVER","*"*20)
                    screen_menu()
                    return
                else:
                    print("Don't quit now, give it another shot")
        # QUESTION 3
        c3 = 0
        while c3 < 2:
            print("Last question,")
            m3 = int(input("How many hours does an average human need to rest?: "))
            if m3 == 8:
                passcode.append(m3)
                print("You really know what you are doing :)")
                print(f"Here is your passcode {passcode}")
                print("*"*20,"!!!CONGRATULATIONS!!!","*"*20)
                return
            else:
                c3 += 1
                if c3 == 2:
                    print("*"*20,"SORRY MATE, GAME OVER, YOU LOSE","*"*20)
                    screen_menu()
                    return
                else:
                    print("Try again")

def Escaping_Guard(a):
    print("Here are some quizzes to help you run away from the guard")
    print("If you get 3 of them correct, congrats you will proceed to next game.")
    q1 = 0
    q2= 0
    q3 = 0
    while q1 < 2:
        riddle1 = str(input("What has a face and hands but no arms and legs"))
        if riddle1 == "clock":
            print("Well done :) Moving to the next one")
            print("RIDDLE 2....")
            while q2 < 2:
                riddle2 = str(input("What has a head and a tail but no body?"))
                if riddle2 == "coin":
                    print("Well done, You're impressive")
                    print("Moving on to the last riddle,",a)
                    while q3 <2:
                        riddle3 = str(input("What goes up but never comes down"))
                        if riddle3 == "age":
                            print("*"*20,"!!!CONGRATULATIONS!!!","*"*20)
                            return
                        else:
                            q3 = q3+1
                            if q3 ==2:
                                print("*"*20,"SORRY MATE!! GAME OVER ","*"*20)
                                return
                            else:
                                print("Try again!!")
                else:
                    q2 = q2 +1
                    if q2 ==2:
                        print("*"*20,"SORRY MATE!! GAME OVER ","*"*20)
                        return
                    else:
                        print("Try again!!")
        else:
            q1 = q1+1
            if q1 ==2:
                print("*"*20,"SORRY MATE!! GAME OVER ","*"*20)
            else:
                print("Try again!!")
# Function for starting the game
def start_game(a,b):
    import random
    print("Starting the game...")
    game_intro()
    print("What are you going to do: ")
    print("1.Work with other prisoners")
    print("2.Move forward by yourself: ")
    print("3.Exit game!!")
    choice = int(input("Choose 1 or 2 or 3: "))
    if choice==1:
        team_route(a,b) 
    elif choice == 2:
        Lone_wolf(a,b)
    elif choice == 3:
        print("Exiting current game section.....")
        screen_menu(a,b)
def screen_menu(a,b):
        
        print("MAIN MENU...")
        print("1. Start Game")
        print("2. Exit Game")
        print("3. View Player Info")
        selection  = str(input("Enter number between 1 and 4 : "))
        while selection != "4":
            #assigning different commands to different responses then outputting the main menu again
            if selection == "1":
                print("Starting the game...")
                start_game(a,b)
                print("MAIN MENU...")
                print("1. Start Game")
                print("2. Exit Game")
                print("3. View Player Info")
                print("4. lopeta")
                selection  = str(input("Enter number between 1 and 4 ,:"))
            elif selection == "2":
                print("Ending the game, see you soon!...")
                return
            elif selection == "3":
                print("Player name =", a)
                print("Age =", b)
                print("MAIN MENU...")
                print("1. Start Game")
                print("2. Exit Game")
                print("3. View Player Info")
                print("4. lopeta")
                selection  = str(input("Enter number between 1 and 4 :"))
        print("No more commands")