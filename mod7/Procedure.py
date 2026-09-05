times = int(input("Enter the number of times you wanna greet:..."))
#name as integer
def greet(times):
    for i in range(times):
        print("Round", i+1, "of saying hello!")
    
print("A new day starts with greetings!")
greet(times)