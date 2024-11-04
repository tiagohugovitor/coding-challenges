# 1255-letterFrequency.py
# Problem: Letter Frequency
# Link: https://judge.beecrowd.com/en/problems/view/1255
# Solved on: 2024-11-03

def letterFrequency():
    tests = int(input())

    for _ in range(tests):
        line = input()
        frequency = {}

        for char in line:
            if char.isalpha():
                char = char.lower()
                if char in frequency:
                    frequency[char] += 1
                else:
                    frequency[char] = 1

        maxFrequency = max(frequency.values())

        charMoreFrequent = sorted([char for char, count in frequency.items() if count == maxFrequency])

        print(''.join(charMoreFrequent))

letterFrequency()