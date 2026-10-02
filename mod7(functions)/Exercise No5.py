def sort(list):
    even_list = []
    for i in range(len(list)):
        #checking if numbers stored at certain points are even and appending them in a new data structure
        if list[i]% 2 == 0:
            even_list.append(list[i])
    return even_list

numbers = [12,23,47,54,87,99,42]
result = sort(numbers)
print("Original list was: ", numbers)
print("New list after removing odd numbers is: ", result)