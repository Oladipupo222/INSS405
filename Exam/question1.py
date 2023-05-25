def collect_inputs():
    numbers = []
    for _ in range(10):
        num = float(input("Enter a number: "))
        numbers.append(num)
    return numbers

def calculate_mean(numbers):
    mean = sum(numbers) / len(numbers)
    return mean

def calculate_sum(numbers):
    total_sum = sum(numbers)
    return total_sum

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        median = sorted_numbers[n // 2]
    return median


input_numbers = collect_inputs()

mean = calculate_mean(input_numbers)

total_sum = calculate_sum(input_numbers)

median = calculate_median(input_numbers)


print("Numbers:", input_numbers)
print("Mean:", mean)
print("Sum:", total_sum)
print("Median:", median)