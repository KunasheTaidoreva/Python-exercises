student = {
    "name":"Kunashe Taidoreva",
    "age":"19",
    "city":"Helsinki"
}

student["name"] = "Esther"
#print(student)
student.pop("city")
print(student.keys())

student["city"] = "Zimbabwe"
print(student.keys())