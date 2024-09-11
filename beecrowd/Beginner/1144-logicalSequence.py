# 1144-logicalSequence.py
# Problem: Logical Sequence
# Link: https://judge.beecrowd.com/en/problems/view/1144
# Solved on: 2024-08-21

def logicalSequence():
    n = int(input())

    for line in range(1, n + 1):
        squared = line ** 2
        cubic = line ** 3
        print(f'{line} {squared} {cubic}')
        print(f'{line} {squared + 1} {cubic + 1}')

logicalSequence()
