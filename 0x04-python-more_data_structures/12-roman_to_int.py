#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "DM": 900,
        "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400
    }
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    result = 0
    prev_value = 0

    for char in reversed(roman_string):
        value = roman_dict[char]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value

    return result
