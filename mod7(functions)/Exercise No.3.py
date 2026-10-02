#funtion To_litres that convert gallons to litres
def To_Litres(gallon):
    litres = gallon * 3.7854
    return litres
gallons = float(input("Enter gasoline gallons: "))
while gallons >= 0:
    x = To_Litres(gallons)
    print(f"{x:.2f}")
    gallons = float(input("Enter gasoline gallons: "))