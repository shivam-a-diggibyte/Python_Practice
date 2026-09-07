# Basic generator function
def simple_generator():
    yield 1
    yield 2
    yield 3

result=simple_generator()
print(result)
print(next(result))

# Practical generator for even numbers 
def even_numbers(limit):

    for number in range(1, limit + 1):

        if number % 2 == 0:
            yield number

for number in even_numbers(10):
    print(number)