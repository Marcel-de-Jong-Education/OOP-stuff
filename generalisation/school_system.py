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
    def __init__(self,name,DoB,rank,title,subject):
        self.name = name
        self.DoB = DoB
        self.rank = rank
        self.title = title
        self.subject = subject
    
    def print_teacher_address(self):
        print(self.rank, self.title, self.name)

    def set_subject(self,subject):
        self.subject = subject

class Student(Person):
    def __init__(self,name,DoB,year,time_table):
        self.name = name
        self.DoB = DoB
        self.year = year
        self.time_table = time_table

    def set_time_table(self,time_table):
        self.time_table = time_table

    def get_time_table(self):
        return self.time_table
    

