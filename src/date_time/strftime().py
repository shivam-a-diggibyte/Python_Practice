from datetime import datetime

now = datetime.now()

formatted_date_time=now.strftime("%d-%m-%y")

print("Formatted date and time:", formatted_date_time)
print("Unformatted date and time:", now)