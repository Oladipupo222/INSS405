num_temperatures = 5

for i in range(num_temperatures):
    temperature = float(input("Enter temperature data: "))

    if temperature >= 50:
        print("Hot")
    elif temperature >= 30 and temperature < 50:
        print("Warm")
    elif temperature >= 0 and temperature < 30:
        print("Cold")
    elif temperature < 0:
        print("Extreme cold")