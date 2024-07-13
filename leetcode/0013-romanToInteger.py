# 0013-romanToInteger.py
# Problem: Roman to Integer
# Link: https://leetcode.com/problems/roman-to-integer/description/
# Solved on: 2024-07-13

# Time complexity: O(n).
# Description: This function iterates through the string s character by character,
# adding or subtracting values based on whether the current value is less than the
# next value in the Roman numeral sequence.

def romanToInteger(s):
    dictionary = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    total = 0
    for i in range(0, len(s)):
        if i+1<len(s) and dictionary[s[i]] < dictionary[s[i+1]]:
            total -= dictionary[s[i]]
        else:
            total += dictionary[s[i]]
    return total
    
print(romanToInteger('MCMXCIV'))