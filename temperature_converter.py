def temperature_converter(temperature, unit):
    if unit.lower() == "celsius":
        return (temperature * 9/5) + 32  # Celsius to Fahrenheit
    elif unit.lower() == "fahrenheit":
        return (temperature - 32) * 5/9  # Fahrenheit to Celsius
    else:
        return "Invalid unit"

print(temperature_converter(25, "Celsius"))  
