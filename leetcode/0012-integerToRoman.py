# 0012-integerToRoman.py
# Problem: Integer to Roman
# Link: https://leetcode.com/problems/integer-to-roman/description/
# Solved on: 2024-07-21

# Time complexity: O(n).
# Space complexity: O(1)
# Description: This function converts an integer to a Roman numeral. It uses a dictionary to map integer values
# to their corresponding Roman numeral representations and iterates through the values in descending order.
# For each value, it repeatedly subtracts it from the given number and appends the corresponding Roman numeral
# to the result string until the given number is reduced to zero.

def intToRoman(num):
    dictionary = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
    }
    values = list(dictionary.keys())
    roman = ''
    
    for value in values:
        while num >= value:
            num = num - value
            roman = roman + dictionary[value]
        
    return roman
    
print(intToRoman(3749))