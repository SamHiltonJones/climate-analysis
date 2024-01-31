# Todo: Code is a bit unclear

def convert_fahr_to_celsius(fahr: float) -> float:
    """
    Given a temperature in Fahrenheit, converts to Celsius
    
    :param fahr: Temperature in fahrenheit
    :raises ValueError: If temp below absolute zero
    :return: The temperature in celsius
    """
    celsius = (fahr - 32) * (5 / 9)
    if celsius < -273.15:
        # If temperature is below absolute zero, throw an error
        raise ValueError(
            f"Trying to convert impossible temperature: {fahr}F"
        )
    return celsius

def convert_fahr_to_kelvin(fahr):
    """
    Given a temperature in Fahrenheit, converts to Kelvin
    
    :param fahr: Temperature in fahrenheit
    :raises ValueError: If temp below absolute zero
    :return: The temperature in kelvin
    """
    celsius = convert_fahr_to_celsius(fahr)
    if celsius < -273.15:
        # If temperature is below absolute zero, throw an error
        raise ValueError(
            f"Trying to convert impossible temperature: {fahr}F"
        )
    kelvin = celsius + 273.15
    return kelvin
