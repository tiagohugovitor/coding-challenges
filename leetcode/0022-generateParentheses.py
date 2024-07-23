# 0022-generateParenthese.py
# Problem: Generate Parentheses
# Link: https://leetcode.com/problems/generate-parentheses/description/
# Solved on: 2024-07-22

# Time complexity: O(4^n / sqrt(n)), n-th Catalan number
# Space complexity: O(4^n / sqrt(n))
# Description: This function generates all combinations of `n` pairs of valid parentheses.
# It uses a recursive helper function `generate` that builds the combinations by adding open and close parentheses
# while maintaining the validity of the sequences. The function ensures that the number of open parentheses 
# never exceeds `n` and that the number of close parentheses never exceeds the number of open parentheses.
# The resulting combinations are stored in the `result` list, which is returned at the end.

def generateParenthesis(n):
    def generate(open, close, answer, construction):
        if open > 0:
            generate(open - 1, close, answer, construction + '(')
        if close > open:
            generate(open, close-1, answer, construction + ')')
        if not (open or close):
            answer.append(construction)
    result = []
    generate(n,n, result, '')
    return result

print(generateParenthesis(3))
