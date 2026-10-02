num = int(input("Enter a number: "))
count = 1
for i in range(num):
    count = count+1
    if num % 2 == 0 or num % 3 ==0:
        print("The number is not prime number")
        break
    else:
        print("The number is prime number")
        break