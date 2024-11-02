# 1141-growingStrings.py
# Problem: Growing Strings
# Link: https://judge.beecrowd.com/en/problems/view/1141
# Solved on: 2024-11-01

# TIME LIMIT EXCEED ISSUE (CHANGE SORT TO INSERT/MERGE)

import sys

def growingStrings():
    input_data = sys.stdin.read().splitlines()
    i = 0

    while i < len(input_data):
        stringsAmount = int(input_data[i])
        i += 1

        if stringsAmount == 0:
            break
            
        strings = input_data[i:i + stringsAmount]
        i += stringsAmount
        
        strings.sort(key=len)

        dp = [len(strings[index]) for index in range(stringsAmount)]

        for index, string in enumerate(strings):
            for j in range(index):
                if strings[j] in string:
                    dp[index] = max(dp[index], dp[j] + 1)

        print(max(dp))

growingStrings()
