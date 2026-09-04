def square(number): #normal function 
    return number * number


print(square(5))

square_lambda = lambda number : number * number #lambda function
print(square_lambda(5));

add = lambda a, b: a + b #lambda function to add two numbers

print(add(10, 20))