import random

def generate_random_integers():
    integers = []
    for _ in range(100):
        num = random.randint(1, 100)
        integers.append(num)
    return integers

def print_odd_numbers(integers):
    odd_numbers = [num for num in integers if num % 2 != 0]
    print("Odd Numbers:", ", ".join(map(str, odd_numbers)))

random_integers = generate_random_integers()

print_odd_numbers(random_integers)