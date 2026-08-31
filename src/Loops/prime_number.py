num = 29
is_prime = True
i = 2
while i < num:
    if num % i == 0:
        is_prime = False
        break
    i += 1
print(num, "is prime:", is_prime)
