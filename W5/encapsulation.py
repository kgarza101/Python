# Encapsulation 

class Student:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        
    # Write a function that changes ID number
        # user ID must be 3 digits long
            # if the input value is invalid, keep the original ID and output message
    def changeID(self, NewID):
        if(NewID > 99 and NewID < 1000): # at least 100
            self.ID = NewID
            print(f"The new ID for {self.name} is {NewID}")
        else:
            print("That's an invalid ID!")       

# Use in a program 
thisStudent = Student("George", 123)

    
# run the function
thisStudent.changeID(846)
    
