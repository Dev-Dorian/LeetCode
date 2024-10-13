import re


def fizzBuzz(n):
    array = []
    for numbers in range(1, n + 1):
        if numbers % 3 == 0 and numbers % 5 == 0:
            array.append("FizzBuzz")
        elif numbers % 3 == 0:
            array.append("Fizz")
        elif numbers % 5 == 0:
            array.append("Buzz")
        else:
            array.append(str(numbers))
    return array


# print(fizzBuzz(10))


def fizzBuzz1(n):
    for numbers in range(1, n + 1):
        if numbers % 3 == 0 and numbers % 5 == 0:
            print("FizzBuzz")
        elif numbers % 3 == 0:
            print("Fizz")
        elif numbers % 5 == 0:
            print("Buzz")
        else:
            print(numbers)


# print(fizzBuzz1(15))


def is_valid_lat_lon(string):
    """
    Checks if a string represents a valid latitude/longitude pair.

    Args:
        string: The string to be checked.

    Returns:
        True if the string is valid, False otherwise.
    """

    # Regular expression for decimal degrees format
    decimal_degrees_pattern = r"^-?\d+\.\d+,-?\d+\.\d+$"

    # Regular expression for degrees, minutes, and seconds format
    dms_pattern = r"^-?\d{1,3}°\d{1,2}'\d{1,2}(\.\d+)?\"[NS],-?\d{1,3}°\d{1,2}'\d{1,2}(\.\d+)?\"[EW]$"

    if re.match(decimal_degrees_pattern, string):
        lat, lon = map(float, string.split(","))
        return -90 <= lat <= 90 and -180 <= lon <= 180
    elif re.match(dms_pattern, string):
        # Implement logic to convert DMS to decimal degrees and validate
        # ...
        print("Hello")
    else:
        return False


# Example usage
strings = ["40.7128,-74.0060",
           "37°47'29.79\"N, 122°24'41.92\"W", "invalid string"]

for string in strings:
    if is_valid_lat_lon(string):
        print(f"{string} is a valid latitude/longitude pair.")
    else:
        print(f"{string} is not a valid latitude/longitude pair.")
