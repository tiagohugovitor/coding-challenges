# 1143-squaredAndCubic.py
# Problem: Squared and Cubic
# Link: https://judge.beecrowd.com/en/problems/view/1143
# Solved on: 2024-08-21

def squaredAndCubic():
    n = int(input())

    for line in range(1, n + 1):
        squared = line ** 2
        cubic = line ** 3
        print(f'{line} {squared} {cubic}')

squaredAndCubic()
