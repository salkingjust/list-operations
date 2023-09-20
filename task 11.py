# m
import list_operations

print("List Operations")
numbers = input("Enter a list of numbers separated by spaces: ").split()

try:
    numbers = [int(num) for num in numbers]
except ValueError:
    print("Invalid input. Please enter a list of valid numbers.")
    exit()

print("1. Find the largest number")
print("2. Find the lowest number")
print("3. Count even numbers")
print("4. Count odd numbers")
print("5. Calculate the sum of numbers")
print("6. Calculate the product of numbers")

choice = input("Enter operation (1/2/3/4/5/6): ")

if choice == '1':
    result = list_operations.find_largest(numbers)
    print(f"The largest number is: {result}")
elif choice == '2':
    result = list_operations.find_lowest(numbers)
    print(f"The lowest number is: {result}")
elif choice == '3':
    result = list_operations.count_even(numbers)
    print(f"Total even numbers: {result}")
elif choice == '4':
    result = list_operations.count_odd(numbers)
    print(f"Total odd numbers: {result}")
elif choice == '5':
    result = list_operations.calculate_sum(numbers)
    print(f"The sum of numbers is: {result}")
elif choice == '6':
    result = list_operations.calculate_product(numbers)
    print(f"The product of numbers is: {result}")
else:
    print("Invalid input")
