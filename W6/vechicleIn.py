from vechicle import *

genericVechicle = Vechicle(3)
myBike = Bicycle()
myTruck = Truck()

print(f"Number of wheels: {myBike.wheels}")
print(f"Number of passengers: {myBike.passengers}")

print(f"Number of wheels: {myTruck.wheels}")
print(f"Number of passengers: {myTruck.passengers}")

genericVechicle.TravelToLocation("London")
myBike.TravelToLocation("Neighbor's house")
myTruck.TravelToLocation("HollyWood")



