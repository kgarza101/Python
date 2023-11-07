# Create datetime date object
import datetime

yesterday = datetime.date(2023, 9, 25)
print(yesterday)

# object for today
today = datetime.date.fromisoformat("2023-09-26")
print(today)

anothertoday = datetime.date.today()
print(anothertoday)

print(yesterday > today)
print(today > yesterday)