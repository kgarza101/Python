# Write a function that will open a file 
    # save the contents of the file in an object
# Use an input parameter to load in a string (the file path)
# print the filepath 
# open file using filepath

def loadText(filepath):
    print(filepath)
    with open(filepath) as f:
        data = f.read()
        return data
    
def replaceTitle(oldText, Newname):
    print(oldText.replace("HAMLET", Newname))