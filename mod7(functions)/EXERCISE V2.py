# List as a variable with a list of floating point numbers
List = [29.6, 75.9, 57.5 , 68.2, 49.23]

# Function average_grade as a function that averages numbers in a given list of numbers
#sum as integer
#avg as float
# i as index of the list
def average_grade(List):
    sum = 0
    avg = 0
    for  i in range(len(List)):
        sum = sum + List[i]
    avg = sum/len(List)
    return avg

#Avg_List to hold the value return by the function average_grade()
Avg_List = []

#adding the average from a list to the list Avg_List
Avg_List.append(average_grade(List))

#outputting the average of the lists stored in the list Avg_List
for i in range(len(Avg_List)):
    print(f"{Avg_List[i]:.2f}")