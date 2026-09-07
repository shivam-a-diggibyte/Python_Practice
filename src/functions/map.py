def square(number): #map applies operation to each and every item in the sequence
    return number * number


numbers = [2, 4, 6, 8]

result = map(square, numbers)

print(list(result))