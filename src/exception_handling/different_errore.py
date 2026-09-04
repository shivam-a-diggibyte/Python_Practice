def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except TypeError:
        print("Both arguments must be numbers")

safe_divide(10, 0)
safe_divide(10, "two")
print(safe_divide(10, 2))
