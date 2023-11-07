with open("CYBI 1\\AliceInWonderLand.txt", "r") as file:
    allText = file.read()
    
reversed_file = allText[::-1]
print(reversed_file)