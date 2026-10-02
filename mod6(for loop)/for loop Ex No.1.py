# asking the user number of times to roll dice
rolls = int(input("Enter number of times to roll dice: "))
import random
# sum as integer to store result of adding numbers from dice
sum = 0
for i in range (rolls):
    side = random.randint(1,6)
    sum = sum + side
# printing out the sum
print("The sum of the rolls is: ", sum)