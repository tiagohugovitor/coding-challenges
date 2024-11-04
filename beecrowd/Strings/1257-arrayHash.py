# 1257-arrayHash.py
# Problem: Array Hash
# Link: https://judge.beecrowd.com/en/problems/view/1257
# Solved on: 2024-11-03

def arrayHash():
    tests = int(input())

    for _ in range(tests):
        totalHash = 0
        words = int(input())
        for element in range(words):
            word = input()
            for position, char in enumerate(word):
                totalHash += (element + position + ord(char) - ord('A'))

        print(totalHash)

arrayHash()