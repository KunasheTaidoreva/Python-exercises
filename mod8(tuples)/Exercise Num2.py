identifier = str(input("Enter a name: "))
names = set()
while identifier != "":
    names.add(identifier)
    identifier = str(input("Enter another name: "))
    for n in names:
        if n == identifier:
            print("Existing name")
            
        else:
            print("New name")
print(".......................")
for n in names:           
    print(n)
