talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))
total_grams = (talents * 20 * 32 * 13.3) + (pounds * 32 * 13.3) + (lots * 13.3)
kilograms = int(total_grams // 1000)
grams = total_grams % 1000
print(f"The weight in modern units: {kilograms} kilograms and {grams:.2f} grams.")