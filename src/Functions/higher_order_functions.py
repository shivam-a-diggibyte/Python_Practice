def square(x): # a function that takes another function as an argument or returns another function is called higher order function
    return x * x


def calculate(function, number):
    return function(number)


print(calculate(square, 5))