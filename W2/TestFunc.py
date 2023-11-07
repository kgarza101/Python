# Import our functions
    # Instead of "#include", use "import"
    
# 3 ways to import 
    # import all functions
    # to use, we need moduleName.functionName()
import stringFunct

# Use our functions
    #1: Take an input string from the user
    #2: Pass that string into our function
    #3: Print the results of each
    
msg = input("Type in your input: ")

theLength = stringFunct.stringLen(msg) 
print(f"your message '{msg}' has a length of {theLength}")
#print(stringLen(msg))

stringFunct.vowelCount(msg)
stringFunct.noSpaces(msg)

