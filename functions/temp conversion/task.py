def to_kelvin(temp_c):
    """Converts a temperature from celsius to kelvin"""
    temp_k = temp_c + 273.15
    return temp_k

def to_fahrenheit(temp_c):
    """Converts a temperature from celsius to farenheit"""
    temp_f = (temp_c * (9 / 5))+ 32
    return temp_f

# You can call functions within functions
def temp_convert(type,temp_c):
    """Takes a temperature in degrees celsius and converts to
    kelvin or fahrenheit given by the paramenter type
    """
    if type == "kelvin":
        return to_kelvin(temp_c)
    elif type == "fahrenheit":
        return to_fahrenheit(temp_c)
    else:
        print("Not a valid temperature type")

# 30 deg celsius is 86 deg Fahrenheit
print(to_fahrenheit(30))

# 30 deg celsius is 303.15 Kelvin
print(temp_convert("kelvin",30))
