def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Shivam"))                       # uses the default greeting
print(greet("Shivam", greeting="Welcome"))    # overrides it by keyword
