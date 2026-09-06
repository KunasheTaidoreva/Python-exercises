s_num = str(input("Enter number: "))
list = []
#checking if value entered is an empty string
while s_num !="":
    #changing the valid parameter from string into an integer and storing it in an array
    num = int(s_num)
    list.append(num)
    s_num = str(input("Enter number: "))
#sorting the list
sorted_list = sorted(list)
#printing the sorted list in reverse order
for i in range(len(sorted_list)-1, -1, -1):
    print(sorted_list[i])