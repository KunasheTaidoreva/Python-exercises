least = 0
most = 0
num_str = str(input("Enter a number: "))
while num_str != " ":
    num = int(num_str)
    if num> most:
        most = num
    if num < least:
        least = num
    num_str = str(input("Enter a number: "))
print(most)
print(least)