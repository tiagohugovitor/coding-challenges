# 3214-sodaSurpler.py
# Problem: Soda Surpler
# Link: https://judge.beecrowd.com/en/problems/view/3214
# Solved on: 2024-10-23

def sodaSurpler():
    empty, found, needed = map(int, input().split())
    drunk = 0
    total = empty + found

    while total >= needed:
        drunk += total // needed
        total = total % needed + total // needed

    print(drunk)

sodaSurpler()
