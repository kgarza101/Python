# Abstractions 
    # the user shouldn't need to know how something works

myList = [1, 2, 3]

# you dotn need to know the mechanics of adding to a list object in order to use this 
myList.append(3)

# part 2 - Inheritance 
# write a class Person
    # every person has name, DOB, favFood
    
class Person:
    def __init__(self, name, DOB, favFood):
        self.name = name
        self.DOB = DOB
        self.favFood = favFood 
        
    def birthday(self):
        if self.favFood == "cake":
            print("Lucky you!")
        else:
            print("Here's some cake anyway.")

# Define a class FootballPlayer
    # Person, except they play for a certain team
    
class FootballPlayer(Person): 
    def birthday(self):
        print("Here's millions of dollars")      
        
# Define a class Child
    # add an attribute to the contructor
class Child(Person):
    def __init__(self, name, DOB, favFood, height = 3):
        # also run all the code of the Person constructor 
        # we can execute the consturctor of the person 
        super().__init__(name, DOB, favFood)
        
        self.height = height  
    