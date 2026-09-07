marks = [65, 85, 90, 72, 95, 60] # filter() function is used to filter item in a sequence based on a condition.

result = filter(lambda mark: mark > 80, marks)

print(list(result))

def is_even(number): # for normal functions
    return number % 2 == 0


numbers = [10, 15, 20, 25, 30]

result = filter(is_even, numbers)

print(list(result))