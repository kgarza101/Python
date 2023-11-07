# Use conditional statments to control flow
## GOAL: take a user input, and display whether this person is:
        # child <13
        # teenager 13 - 19
        # adult >19
# You shouldn't get a type error
# You should only output one statment 
# If the user gives an invalid input, print an error statment
# KEep asking user for an age until value is apprporiate 
number = -1
while(number < 0):        
        try:
                number = int(input("Type in your age: "))
                if number < 0:
                        print("Number must be postive")
        except:
                print("That's an invalid number! Please try again...")
                number = -1
                
                
if (number < 13):
        print("Child")
elif (number < 20):
        print("Teenager")
else:
        print("Adult")


# Try/except
# try:
#         x = "Chocolate" % 2  
# except:
#         print("Chocolate is not a number!") 
        