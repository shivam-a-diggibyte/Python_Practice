import datetime

today = datetime.date.today()

print(' Today date is :',today)

 # Use of datetime function
import datetime

now = datetime.datetime.now()

print(now)

# Use of timedelta function
import datetime

today = datetime.date.today()

tomorrow = today + datetime.timedelta(days=1)

print("Today:", today)
print("Tomorrow:", tomorrow)