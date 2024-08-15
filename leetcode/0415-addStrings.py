# 0415-addStrings.py
# Problem: Add Strings
# Link: https://leetcode.com/problems/add-strings/description/
# Solved on: 2024-08-15

# Time complexity: O(max(n, m))
# Space complexity: O(max(n, m))
# Description: This function adds two non-negative integers represented as strings (`num1` and `num2`) and returns the 
# result as a string. It simulates manual addition by iterating through both strings from right to left, adding corresponding 
# digits along with any carry. If one string is shorter, it continues to add the remaining digits of the longer string. 
# Finally, if there's a carry left, it's added to the front of the result. The time and space complexity depend on the 
# length of the longer string.

def addStrings(num1, num2):
    carry = 0
    result = ''
    p = len(num1) - 1
    q = len(num2) - 1
    while p >= 0 and q >= 0:
        sum = ord(num1[p]) - ord('0') + ord(num2[q]) - ord('0') + carry
        result = str(sum%10) + result
        carry = sum // 10
        p -= 1
        q -= 1

    while p >= 0:
        sum = ord(num1[p]) - ord('0') + carry
        result = str(sum%10) + result
        carry = sum // 10
        p -= 1

    while q >= 0:
        sum = ord(num2[q]) - ord('0') + carry
        result = str(sum%10) + result
        carry = sum // 10
        q -= 1

    if carry == 1:
        result = '1' + result

    return result

print(addStrings('11', '22'))