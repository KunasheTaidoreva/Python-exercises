Answer = str(input("Are you a citizen of the country? (yes/no)...."))
if Answer=="yes":
    age = int(input("Enter you age"))
    if age >= 18:
        print("You are eligible to vote")
    else:
        print("You are underage to vote sorry!")
else:
    print("You arent eligible to vote sorry!")