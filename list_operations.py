# list_operations.py

def find_largest(numbers):
    if not numbers:
        return None
    return max(numbers)

def find_lowest(numbers):
    if not numbers:
        return None
    return min(numbers)

def count_even(numbers):
    return len([x for x in numbers if x % 2 == 0])

def count_odd(numbers):
    return len([x for x in numbers if x % 2 != 0])

def calculate_sum(numbers):
    return sum(numbers)

def calculate_product(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result
