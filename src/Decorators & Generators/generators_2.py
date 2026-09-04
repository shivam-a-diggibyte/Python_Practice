squares_gen = (x * x for x in range(5))

print("Generator object:", squares_gen)

print("Values from generator:", next(squares_gen))
print("Values from generator:", list(squares_gen))