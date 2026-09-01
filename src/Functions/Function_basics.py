def greet():   # basic function with no paramenters
    print("Hello, Shivam!")


greet()

def greet(name):    #function with paramenters 
    print(f"Hello, {name}!")


greet("Shivam")

def add(a, b): #function with a return value
    return a + b


result = add(10, 20)
print("Result:", result)