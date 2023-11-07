# define a class, student
# tie anything to the class by using "self"

class student:
    # add some atrributes
        # name
        # SID
        # major
        # undergraduate Y/N        
        
    # constructor meethod
    def __init__(self, name = "something", SID = 123, major = "undeclared", undergraduate = True):
        self.name = name
        self.SID = SID
        self.major = major
        self.undergraduate = undergraduate        
        
    # define a method changename()
        # input parameter should be new name
        # overwrite the old name value
    def changename(self, newname):
        self.name = newname
        
    # define a method greet() that prints a hello messasage
    def greet(self):
        print("Hello there.")
        
    # notes (runs only if i execute student.py directly)
    #   if __name__ == "__main__":
    #        print("hello")
    
class Course:
    def __init__(self, coursename = "CS111", studentlist = [student()]):
        self.coursename = coursename
        self.studentlist = studentlist