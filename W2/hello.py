# This is a single line comment
'''
This
is a
multi-lined comment
'''

# I/O
print('Hello') # Single quotes
print("Hello") # Double quotes
print('Greg\'s notbook')

# Objects/Varibles 
# Store the number 9 in an object
x = 9

# Store a name - Tom
# Store a letter - u
# Store a decimal value - 7.2
name = "Tom"
letter = "u"
value = 7.2

# What will happen?
x = "Tom"
x = 7.2
x = letter
x = 7

# Increment an integer
x += 1
print(x)
x = x+1 
print(x)

# White space matters
# New line for each instruction
# 'TAB' character is used for code block
if True:
    x+=1
    print("Hello")
    print("Goodbye")
    
# I/O formatted strings
a = 1
b = 2

#P Print all 3 values a, b, x
print(a)
print(b)
print(x) 
print(a, b, x)

# The values of a, b, and x are 1, 2, and 7
print("The values of a, b, and x are", a, b, "and", x,)

# Alternative - use an f-string
print(f"The values of a, b, an x are {a}, {b}, and {x}")

# Expressions work as well
print(f"If we add a and b, we get {a+b}")

#Can we use other datatypes? 
print(f"Here are some objects: {a}, {name}, {letter}")

# Take input from the consle
x = input("Please enter a number: ")

# Check the datatype of x
print(type(x))

# Change a string to a number 
# Typecasting 
x = int(x)
print(type(x))
print(x+1)

# Goal: Take input from console, cast to integer, save as "a"
a = int(input("Please enter another number: "))

# EX1: Ask the user for their name and favorite number
# Show the user a greeting by name and show them 1000x their number
name1 = input("Enter your name: ") 
num1 = int(input("Enter your favorite number: "))
print(f"Hello {name1}, your favorite number x1000 is {num1 * 1000}.")

# If the user's number is even, print "That's an even number"
# If not the number is odd. 
if (num1 % 2 == 0):
    print("Even")    
elif(num>10):
    print("Larger number")
else:
    print("Odd")
print("Last message")

# If not the user's number is greater than 10


    
    







