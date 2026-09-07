def calculate_average(marks: list[int]) -> float: # tells marks is a list having integer values and return float type

    return sum(marks) / len(marks)

result: float = calculate_average([80, 90, 70])
print("Average:", result)
