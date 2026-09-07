def add(a, b):
    """Return the sum of two numbers.""" # it is a docstring which descibes the function.
    return a + b

def calculate_average(marks):
    """Return the average of a list of numeric marks. # it is a docstring which descibes the function.

    Args:
        marks: a list of numbers.

    Returns:
        The arithmetic mean of the list.
    """
    return sum(marks) / len(marks)

print(calculate_average([80, 90, 70]))
print(calculate_average.__doc__)
