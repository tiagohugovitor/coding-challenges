# 1065-evenBetweenFiveNumbers.py
# Problem: Even Between five Numbers
# Link: https://judge.beecrowd.com/en/problems/view/1065
# Solved on: 2024-08-19

def evenBetweenFiveNumbers():
    count = 0

    for _ in range(0, 5):
        value = float(input())
        if value % 2 == 0:
            count += 1


    print(f'{count} valores pares')

evenBetweenFiveNumbers()