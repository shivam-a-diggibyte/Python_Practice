from datetime import datetime,timedelta

now = datetime.now()
future_day= now + timedelta(days=7)

print("Future day:", future_day)
print("Today's day:", now)
