class Person:
    def __init__(self,name):
        self.name = name
    def introduce(self):
        print("My name is",self.name)

class Student(Person):
    def __init__(self,name,course):
        self.course = course
        super().__init__(name)
    def introduce(self):
        print("My name is",self.name,"and l study",self.course)


s1 = Student("Kunashe","IT")
s1.introduce()