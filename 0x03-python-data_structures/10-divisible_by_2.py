#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return None
    result = []
    for number in my_list:
        result.append(number % 2 == 0)
    return result
