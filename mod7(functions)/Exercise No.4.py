def sum(Numbers):
    total = 0
    for i in range(len(Numbers)):
        total = total + Numbers[i]
    return total

list =[12,45,66,78,10,6]
result = sum(list)
print("The sum of values in the list is", result)