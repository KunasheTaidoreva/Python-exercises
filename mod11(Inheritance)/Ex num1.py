class Publication:
    def __init__(self,author):
        self.author= author

class Book(Publication):
    def __init__(self,name,author,page_count):
        super().__init__(author)
        self.name =name
        self.page_count = page_count
    def print_information(self):
        print("The author is",self.author,"it has",self.page_count,"pages")

class Magazine(Publication):
    def __init__(self,name,author):
        super().__init__(author)
        self.name =name
    def print_information(self):
        print("The chief editor is",self.author,"it was written by",self.name)

m1 = Magazine("Donald Duck","Aki Hyyppa")
m1.print_information()
b1 = Book("Compartment No.6","Rosa Liksom",192)
b1.print_information()
