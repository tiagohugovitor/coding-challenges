# 1237-compareSubstring.py
# Problem: Compare Substring
# Link: https://judge.beecrowd.com/en/problems/view/1237
# Solved on: 2024-11-04

import sys

def compareSubstring():
    input = sys.stdin.read
    data = input().splitlines()
    
    i = 0

    while i < len(data):
        firstString = data[i]
        i += 1
        secondString = data[i]
        i += 1

        m = len(firstString)
        maxLength = 0

        for start in range(m):
            for end in range(start + 1, m + 1):
                substring = firstString[start:end]
                if substring in secondString:
                    maxLength = max(maxLength, end - start)
                else:
                    break


        print(maxLength)
    
compareSubstring()