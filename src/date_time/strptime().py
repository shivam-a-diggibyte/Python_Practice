from datetime import datetime

date_text = "08-09-2026"

parsed = datetime.strptime(date_text, "%d-%m-%Y")

print("Text:", date_text)

print("Parsed datetime object:", parsed)

print("Day of week:", parsed.strftime("%A"))
