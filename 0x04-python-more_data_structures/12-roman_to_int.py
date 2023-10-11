#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_d = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000}
    tot = 0
    prev_val = 0
    for num in reversed(roman_string):
        val = roman_d.get(num, 0)
        if val < prev_val:
            tot -= val
        else:
            tot += val
        prev_val = val
    return tot
