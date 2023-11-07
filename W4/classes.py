# Object Oriented Programming
    # instead of carrying our instructions 
    # applications will have a "state"
        # based on the state, objects will behave and react in certain ways
        
# basic structure
#   while(True):
#       myObject.run()
#       if myObject.done:
#       exit()
    

# import student object definition
from student import student

# declare a student object
mystudent = student()

# access name attribute of student object
print(mystudent.name)

# change the name of the student
mystudent.changename("Berto")

# print the new name
print(mystudent.name)

mystudent.greet()

# declare a new student with custom info
otherstudent = student("Jerma", 985, "Math", False)

# print the name of the student
print(otherstudent.name)

# change the major to CS
otherstudent.major = "CS"

# define a class course
    # attributes 
        # course name
        # list of students
        
# constructor 
    # default coures name of CS1111
    # default list of students [Student]

class Course:
    def __init__(self, coursename = "CS111", studentlist = [student()]):
        self.coursename = coursename
        self.studentlist = studentlist
        
        

                        
    