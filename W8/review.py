# random number generator
import random 

WINDOW_WIDTH = 800
myNum = random.randint(0, WINDOW_WIDTH)

for x in range(100):
    print(myNum)
    myNum = random.randint(0, WINDOW_WIDTH)
    
# Types in python
x = False # x is only booleon

# to cast a type
print(x)
print(type(x))
print(type(str(x)))    

# input() function
# make sure to assign to save imput
# always a integer
somethingObj = float(input("Please enter something: "))

# Try/except
x = 10
try:
    x < 5 # there is no error here, even if it is false
    print("Hooray")
except:
    print("ERROR")
    
# Branches 
# if number is odd print odd
# if number is odd and addiational over 100 
    # print weird
# in all other cases multiple the number by 10 and print it
if(x%2 == 1):
    if(x > 100):
        print("weird")
    else:
        print("odd")
else:
    print(f"The number is: {10 * x}")
    
# Print all numbers from 0 to 40
for x in range(0, 40):
    print(x)
    
# Print all multiples of 3 from 0 to 40
# init
x = 0
while(x < 40):
    print(x)
    # update
    x += 3
    
# Fill a list with numbers from 10 to -10
myList = []
x = 10
while(x >= -10):
    # add the number to the list
    myList.append(x)
    x -= 1
    
# print each element in the list
for x in myList:
    print(x)
    
print(myList)

# Use index to print each element in the list
length = len(myList) # find how many values in list
for x in range(length): 
    print(myList[x])
print(len(myList))
        

    