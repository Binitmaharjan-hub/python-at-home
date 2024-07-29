def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
celsius_temp = int(input("enter a number:"))
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is {fahrenheit_temp}°F")
