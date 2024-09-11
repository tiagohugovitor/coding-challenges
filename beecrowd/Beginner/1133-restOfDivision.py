# 1133-restOfDivision.py
# Problem: Rest of a Division
# Link: https://judge.beecrowd.com/en/problems/view/1133
# Solved on: 2024-08-21

def restOfDivision():
    x = int(input())
    y = int(input())

    if y < x:
        x, y = y, x

    for i in range(x + 1, y):
        rest = i % 5
        if rest == 2 or rest == 3:
            print(f'{i}')

restOfDivision()
