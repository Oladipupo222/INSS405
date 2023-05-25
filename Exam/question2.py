import random

def generate_random_numbers():
    numbers = []
    for _ in range(100):
        num = random.randint(1, 1000)
        numbers.append(num)
    return numbers

def sort_numbers(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers

random_numbers = generate_random_numbers()

sorted_numbers = sort_numbers(random_numbers)

print("Random Numbers:", random_numbers)
print("Sorted Numbers:", sorted_numbers)