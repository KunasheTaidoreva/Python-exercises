def dice():
    import random
    x = random.randint(1,6)
    return x

roll = dice()
while roll != 6:
    print(roll)
    roll = dice()
    if roll == 6:
        print(6)