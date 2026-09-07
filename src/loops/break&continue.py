# break and continue
for n in range(10):
    if n == 5:
        break        # stop the loop completely
    if n % 2 == 0:
        continue     # skip even numbers, go to next iteration
    print(n)
