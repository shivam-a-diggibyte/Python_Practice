import calculator

a= int(input('Enter first number:')) # you have to define type of input a as by default input will be stored as string then error will be shown.
b= int(input('Enter second number:'))

result = calculator.mul(a,b)

print('Multiplication of', a, 'and', b, 'is', result)