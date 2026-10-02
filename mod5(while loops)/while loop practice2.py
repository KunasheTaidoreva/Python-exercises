command= input("Enter command!")
while command != "stop":
    if command == "MAYDAY":
        break
    print("Executing command: "+command)
    command = input("Enter command: ")
else:
    print("This is the execution of the else block normally")
print("Execution stopped.")