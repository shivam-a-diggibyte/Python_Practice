try:
    value = int("abc")
except ValueError as e:
    print("Error:", e)
else:
    print("No error occurred")
finally:  # it is always executed whether an exception occurs or not
    print("This always runs")
