import datetime,date,calendar
import math 
now = datetime.datetime.now()
print(now)
# print(datetime.datetime.now())
# print(calendar.calendar(2015))

formatted=now.strftime("%d|%B|%Y")

print(formatted)


print(math.sqrt(64))