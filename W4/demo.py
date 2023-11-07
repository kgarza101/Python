# mylist = [1, 2, 3, 4]

# mylist.append(10)
# print(mylist)


mylist = ["Acount Created", "Deposit: $25\t", "Balance: $25"]
deposit = 5
balance = 25

mylist.append(f"Deposit: {deposit}\t Balance {balance + deposit}")

for transaction in mylist:
    print(transaction)
    
# remove index 1 from my list 
mylist.pop(0)

for transaction in mylist:
    print(transaction)
    
    
    # define a class TV
    # attributes 
        # size
        # brand
        # is 4k (Y/N)
    # define constructor
        # set defaults: 
            # size: 5
            # brand: HEB
            # is4k: Yes
class TV:
    def __int__(self, size = 5, brand = "HEB", is4k = True):
        self.size = size
        self.brand = brand
        self.is4k = is4k