def add_all(*args): # variable number of parameters will be paased as a tuple and will be added
    return sum(args)


print(add_all(1, 2, 3, 4))

def show_args(*args): #verify that type of argument is tuple
    print(args)
    print(type(args))


show_args(10, 20, 30)

def show_numbers(*args): #accessing individual elements of the argument as it is stored as a tuple
    print("First number:", args[0])
    print("Second number:", args[1])


show_numbers(10, 20, 30)