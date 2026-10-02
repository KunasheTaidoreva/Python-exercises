print("Would you like to: 1.Enter a new airport")
print("                   2.Fetch information for an existing airport")
print("                   3.QUIT")
choice = int(input("Enter the number of your choice: "))
AIRPORTS = []
while choice != 3:
    if choice ==1:
        code = str(input("Enter ICAO code"))
        name = str(input("Enter airport name"))
        new_airport = {"ICAO code":code,
                       "Airport name":name}
        AIRPORTS.append(new_airport)
    else:
        Ex_code = str(input("Enter the ICAO of the existing airport"))
        for i in range (len(AIRPORTS)):
            if AIRPORTS[i]["ICAO code"] == Ex_code:
                print(AIRPORTS[i]["Airport name"])
    print("What would you like to do again: 1.Enter a new airport")
    print("                                 2.Fetch information for an existing airport")
    print("                                 3.QUIT")
    choice = int(input("Enter the number of your choice: "))