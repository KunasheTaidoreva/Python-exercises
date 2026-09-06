# array cities to store names of cities entered by user
cities = []
for i in range(5):
    name = str(input("Enter the name of city: "))
    #storing the names of cities in the array
    cities.append(name)
for i in range(5):
    print(cities[i])
