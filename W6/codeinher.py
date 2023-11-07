from codegrade import *

std = CodeGradeUser("John", "Code University")

std.hello()

devin = Student("Devin", "University of Amsterdam", 2018)
devin.graduated()

devin.handin("Python Assignment")

robin = Teacher("Robin", "Code University")

robin.teach()
robin.grade(devin, 90)

peter = Student("Peter", "Code University", 2018)
robin.grade(peter, 85)