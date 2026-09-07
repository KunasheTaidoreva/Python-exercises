def Pizza(diameter,price):
    radius = (diameter/2)/100
    area = 3.14*radius**2
    unit_price = price/area
    return f"{unit_price:.2f}"

diameter1 = int(input("Enter the diameter of first pizza: "))
price1 = float(input("Enter the price of the first pizza: "))
first = Pizza(diameter1,price1)
diameter2 = int(input("Enter the diameter of second pizza: "))
price2 = float(input("Enter the price of the second pizza: "))
second = Pizza(diameter2,price2)
if first < second:
    print("The first pizza is better because it costs $",first,"/square meter while the second one costs $",second,"/square meter")
else:
    print("The second pizza is better because it costs $",second,"/square meter while the first one costs $",first,"/square meter")