class Cat:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    def meow(self):
        print(f"{self.name} says: Meow!")