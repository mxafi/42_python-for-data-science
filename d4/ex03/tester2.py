from new_student import Student

# $> python tester.py
# ...
# TypeError: Student.__init__() got an unexpected keyword argument 'id'
# $>

student = Student(name="Edward", surname="agle", id="toto")
print(student)
