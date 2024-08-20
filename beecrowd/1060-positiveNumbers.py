# 1060-positiveNumbers.py
# Problem: Positive Numbers
# Link: https://judge.beecrowd.com/en/problems/view/1060
# Solved on: 2024-08-19

def positiveNumbers():
    count = 0

    for i in range(0, 6):
        value = float(input())
        if value > 0:
            count += 1

    print(f'{count} valores positivos')

positiveNumbers()