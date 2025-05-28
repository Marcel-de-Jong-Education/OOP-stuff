import school_system as s

student0 = s.Student("Heyhai Kirakira", "2007-04-09", 12, ["Maths", "English", "Art Studies"])

teacher0 = s.Teacher("Robert Smithysmith", "1989-02-28", "Department Head", "Mr", "Art Studies")

print("Teacher:")
teacher0.print_teacher_address()


print("Student:", student0.name,"\nTimetable:\n",student0.get_time_table())
