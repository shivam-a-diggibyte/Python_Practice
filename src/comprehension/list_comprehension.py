# normal approach
numbers = [1,2,3,4,5]

squares=[]
for i in numbers:
    squares.append(i**2)

print(squares)

# using list comprehensions

a =[2,4,6,8,25]

squares=[i**2 for i in a]

print(squares)