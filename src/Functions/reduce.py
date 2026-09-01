from functools import reduce # functools module need to be imported to use reduce function

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda a, b: a + b, numbers) # reduce() function is used to reduce output to a single value 

print(result)

from functools import reduce


def mul(a, b):
    return a * b


numbers = [10, 20, 30, 40]

result = reduce(mul, numbers)

print(result)