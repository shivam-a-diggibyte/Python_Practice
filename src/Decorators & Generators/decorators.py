def log_function(func):

    def wrapper():
        print(f"Calling function: {func.__name__}") # tells the name of the function being called

        func()

        print(f"Finished function: {func.__name__}")

    return wrapper


@log_function
def greet():
    print("Hello Shivam!")


greet()


def my_decorator(func):

    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Shivam")













