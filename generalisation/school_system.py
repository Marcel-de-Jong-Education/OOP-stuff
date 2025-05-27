class Person:
    def __init__(self,name,DoB):
        self.name = name
        self.DoB = DoB
    
    def display_details(self):
        print
        (
            "Name:", self.name,
            "\nDate of Birth:", self.DoB
        )
    
class Teacher(Person):
    def __init__(self, rank, title):

