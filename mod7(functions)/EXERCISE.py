# Function that averages
#numbers as a list of numbers
numbers = [13.3, 44.6,57.0, 0.56, 49.2]
def Average(numbers):
    total = 0
    avg = 0
    for i in range(5):
        total = total + numbers[i]
    avg = total/5
    return avg
# result to hold the value return by the function Average()
result=Average(numbers)
print("The average of the numbers is: ", f"{result:.2f}")