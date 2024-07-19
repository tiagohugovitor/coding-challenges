# 0066-plusOne.py
# Problem: Plus One
# Link: https://leetcode.com/problems/plus-one/description/
# Solved on: 2024-07-18

# Time complexity: O(n)
# Space complexity: O(n)
# Description: This function increments the number represented by a list of digits by one.
# It handles the carry-over for each digit and adjusts the list size if necessary to 
# accommodate an additional digit when there is an overflow (e.g., from 999 to 1000).

def plusOne(digits):
    carry = 1
    i = len(digits) - 1
    while carry == 1 and i >= 0:
        carry, digits[i] = (digits[i] + carry)//10, (digits[i] + carry)%10
        i -= 1

    if carry == 1:
        i = len(digits)
        answer = [0] * (i + 1)
        while i > 0:
            answer[i] = digits[i-1]
            i -= 1
        answer[0] = carry
        return answer

    return digits

    

print(plusOne([9,9,9]))