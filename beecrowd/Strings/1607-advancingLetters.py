# 1607-advancingLetters.py
# Problem: Advancing Letters
# Link: https://judge.beecrowd.com/en/problems/view/1607
# Solved on: 2024-11-04

def advancingLetters():
    tests = int(input())

    for _ in range(tests):
        stringA, stringB = input().split()
        totalOperations = 0
        for index, char in enumerate(stringA):
            if char == stringB[index]:
                continue
            difference = ord(stringB[index]) - ord(char)
            totalOperations += difference
            if difference < 0:
                totalOperations += 26

        print(totalOperations)

advancingLetters()