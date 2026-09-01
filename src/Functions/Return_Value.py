def add(a, b): #single return value
    return a + b

result = add(5, 7)
print(result)     # 12


def calculate(a, b): #multiple return values
    addition = a + b
    multiplication = a * b

    return addition, multiplication


add_result, multiply_result = calculate(10, 5)

print("Addition:", add_result)
print("Multiplication:", multiply_result)