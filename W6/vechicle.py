class Vechicle:
    def __init__(self, wheels = 2):
        self.wheels = wheels
        
        if(wheels < 2):
            self.passengers = 1
            
        elif(wheels < 4):
            self.passengers = 2
        
        elif(wheels < 18):
            self.passengers = 9
            
        else:
            print("We shouldn't be here")
            self.passengers = 0
            
# Abstract method (regular method for now )
    # TravelToLocation
        # input parameter of destination 
        # print {number of passengers} are being trasnported to {desintation}
    def TravelToLocation(self, destination):
        print(f"{self.passengers} are being tranported to {destination}.")
        
# Bicycle class (2 wheels)
    # Overwrite the TravelToLocation method
    # print different message 
    
# Truck class (4 wheels)
    # add a "hp" attribute to the contructor (use input parameter)
    # if "hp" is below 10, when travel to location is exeucted, print an error 
     # otherwise run as normal 

class Bicycle(Vechicle):
    def __init__(self):
        super().__init__(wheels = 2)
        
    def TravelToLocation(self, destination):
        print(f"Wheeling over to {destination}!")

    
class Truck(Vechicle):             
    def __init__(self, hp):
        super().__init__(wheels = 4)
        self.hp = hp
        
    def TravelToLocation(self, destination):
        if(self.hp > 10):
            super().TravelToLocation(destination)
        else:
            print("There is no power.")

            