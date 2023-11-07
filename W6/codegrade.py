from datetime import * 

class CodeGradeUser:
    def __init__(self, username, institution):
        self.username = username
        self.institution = institution

    def hello(self):
        print(f"Hello {self.username} from {self.institution}")

class Student(CodeGradeUser):
    def __init__(self, username, institution, graduation_year):
        super().__init__(username, institution)
        self.graduation_year = graduation_year
        
    def graduated(self):
        student_year = datetime.today().year
        
        if(student_year > self.graduation_year):
            return True
        else: 
            return False

    def handin(self, assignment):
        if self.graduated():
            print(f"Thanks, {self.username}! Your submission {assignment} was successfuly handed in!")
        else:
            print(f"Sorry {self.username}, you can only hand in if you haven't graduated yet!")

class Teacher(CodeGradeUser):
    def teach(self):
        print("Did you know Python was named after the British comedy group Monty Python?")
        
    def grade(self, student, grade):
        if self.institution == student.institution:
            print(f"{self.username} graded {student.username} with grade {grade}")
        else:
            print(f"You cannot grade {self.username} as they are from another institute..")
        
        
    