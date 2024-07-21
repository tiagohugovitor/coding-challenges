# 0017-letterCombinations.py
# Problem: Letter Combinations of a Phone Number
# Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# Solved on: 2024-07-21

# Time complexity: O(4^n * n), where n is the length of the input digits.
# Space complexity: O(n), where n is the length of the input digits.
# Description: This function generates all possible letter combinations that the number could represent.
# It uses a dictionary to map each digit to its corresponding letters and a divide-and-conquer approach
# to recursively generate combinations. The function combines results from subproblems to form the final output.

def letterCombinationsDivideAndConquer(digits):
    dictionary = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }

    def combine(left, right):
        combinations = []
        for first in left:
            for second in right:
                combinations.append(first+second)
        return combinations

    def letterCombinations(subdigits):
        if len(subdigits) == 0:
            return []
        if len(subdigits) == 1:
            return dictionary[subdigits[0]]
        mid = len(subdigits) // 2
        left = letterCombinations(subdigits[:mid])
        right = letterCombinations(subdigits[mid:])
        return combine(left, right)

    return letterCombinations(digits)

# Time complexity: O(4^n)
# Space complexity: O(4^n)
# Description: This function generates all possible letter combinations that a number could represent.
# It uses a dictionary to map each digit to its corresponding letters and iteratively builds combinations.

def letterCombinationsIterative(digits):
    if len(digits) == 0:
        return []

    dictionary = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }

    combinations = dictionary[digits[0]]
    
    for digit in range(1, len(digits)):
        newCombinations = []
        for combination in combinations:
            for new in dictionary[digits[digit]]:
                newCombinations.append(combination+new)
        combinations = newCombinations
    
    return combinations

print(letterCombinationsIterative('23'))
