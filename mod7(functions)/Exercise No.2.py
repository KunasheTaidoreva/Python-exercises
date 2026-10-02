#SidesNumber as integer
SidesNumber = int(input("Enter the number of sides on your dice "))
def dice(SidesNumber):
    import random
    x = random.randint(1, SidesNumber)
    return x

roll = dice(SidesNumber)
while roll != SidesNumber:
    print(roll)
    roll = dice(SidesNumber)
    if roll == SidesNumber:
        print(SidesNumber)