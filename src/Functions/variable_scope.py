def calculate():
    total = 100        # local to this function
    return total

print(calculate())    # 100
# print(total)        # error — total doesn't exist out here
