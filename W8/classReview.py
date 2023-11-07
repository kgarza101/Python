# define a class Computer
    # attributes:
    # ram, screenres. price, brand
# define a class Smartphone
    #same as computer but phone number
    
class Computer:
    def __init__(self, ram, screenres, price, brand = "HP"):
        self.ram = ram
        self.screenres = screenres
        self.price = price
        self.brand = brand

class Smartphone(Computer):
    def __init__(self, ram, screenres, price, phonenum, brand="HP"):
        super().__init__(ram, screenres, price, brand)
        self.phonenum = phonenum

