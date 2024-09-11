# 1059-evenNumbers.py
# Problem: Even Numbers
# Link: https://judge.beecrowd.com/en/problems/view/1059
# Solved on: 2024-08-19

def evenNumbers():

    for i in range(1, 101):
        if i % 2 == 0:
            print(f'{i}')

evenNumbers()