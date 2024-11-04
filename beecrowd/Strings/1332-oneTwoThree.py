# 1332-oneTwoThree.py
# Problem: One-Two-Three
# Link: https://judge.beecrowd.com/en/problems/view/1332
# Solved on: 2024-11-03

def oneTwoThree():
    tests = int(input())

    numbers = ['one', 'two', 'three']
    stringToInt = {
        'one': '1',
        'two': '2',
        'three': '3',
    }

    for _ in range(tests):
        written = input()

        for correctSpell in numbers:
            differences = 0
            for index, char in enumerate(correctSpell):
                if index >= len(written) or char != written[index]:
                    differences += 1
                if differences > 1:
                    break
            if differences <= 1:
                print(stringToInt[correctSpell])

oneTwoThree()