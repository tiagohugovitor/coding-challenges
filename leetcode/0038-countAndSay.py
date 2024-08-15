# 0038-countAndSay.py
# Problem: Count and Say
# Link: https://leetcode.com/problems/count-and-say/description/
# Solved on: 2024-08-14

# Time complexity: O(2^n)
# Space complexity: O(2^n)
# Description: This function generates the nth term of the "Count and Say" sequence using run-length encoding (RLE).
# The rle function counts consecutive characters and builds the resulting string. The time and space complexity is O(2^n)
# due to the exponential growth of the sequence length. The function uses a recursive top-down approach.

def countAndSay(n):
    def rle(string):
        countAndSayString = ''
        count = 1
        lastChar = string[0]
        for i in range(1, len(string)):
            char = string[i]
            if char == lastChar:
                count += 1
            else:
                countAndSayString += str(count) + lastChar
                lastChar = char
                count = 1
        countAndSayString += str(count) + lastChar
        return countAndSayString

    if n == 1:
        return '1'

    return rle(countAndSay((n-1)))

print(countAndSay(4))
