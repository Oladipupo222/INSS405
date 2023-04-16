def get_temperature():
    temperature = float(input("Enter temperature : "))
    return temperature

def determine_temperature_category(temperature):
    if temperature < 30:
        return "Cold"
    elif temperature < 40:
        return "Warm"
    elif temperature > 50:
        return "Hot"

def print_temperature_category(category):
    print(category)


temperature = get_temperature()


category = determine_temperature_category(temperature)


print_temperature_category(category)