from  abstractions import *
#Person, FootballPlayer, Child

me = Person("My name", -1000, "Rice")
me.birthday()

notMe = FootballPlayer("Not me", 1999, "footballs")
notMe.birthday()

kid = Child("idk", 2023, "pizza", 4)
print(kid.name)