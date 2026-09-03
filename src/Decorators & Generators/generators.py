def log_function(func):

    def wrapper():
        print(f"Calling function: {func.__name__}")

        func()

        print(f"Finished function: {func.__name__}")

    return wrapper


@log_function
def greet():
    print("Hello Shivam!")


greet()