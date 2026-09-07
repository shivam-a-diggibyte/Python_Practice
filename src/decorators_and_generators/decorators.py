# decorator for measuring time.
import time
from functools import wraps


def measure_time(function):

    @wraps(function) # to protect the metadata of the original function
    def wrapper(*args, **kwargs): # wrapper
        start = time.time()

        result = function(*args, **kwargs)

        end = time.time()

        print(f"Execution time: {end - start:.4f} seconds")

        return result

    return wrapper


@measure_time
def calculate_sum():
    total = 0

    for number in range(1_000_000):
        total += number

    return total


print(calculate_sum())