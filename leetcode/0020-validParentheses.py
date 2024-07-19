# 0020-validParentheses.py
# Problem: Valid Parentheses
# Link: https://leetcode.com/problems/valid-parentheses/description/
# Solved on: 2024-07-19

# Time complexity: O(n)
# Space complexity: O(n)
# Description: This function checks if a given string of parentheses is valid.
# It uses a stack to keep track of opening parentheses. When a closing parenthesis is encountered,
# it checks if it matches the most recent opening parenthesis on the stack. If it does not match
# or the stack is empty when a closing parenthesis is found, the function returns False.
# If the stack is empty at the end, it means all parentheses were properly closed and nested, and the function returns True.

def validParentheses(s):
    closure = {
        '(': ')',
        '{': '}',
        '[': ']',
    }
    stack = []
    for char in s:
        if char in ('(', '{', '['):
            stack.append(char)
        else:
            if len(stack) == 0 or closure[stack.pop()] != char:
                return False
    return True if len(stack) == 0 else False

print(validParentheses(')'))