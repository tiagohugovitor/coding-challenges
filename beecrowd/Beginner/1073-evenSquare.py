# 1073-evenSquare.py
# Problem: Even Square
# Link: https://judge.beecrowd.com/en/problems/view/1073
# Solved on: 2024-08-19

def evenSquare():
    n = int(input())

    for i in range(2, n + 1, 2):
        print(f'{i}^2 = {(i*i):.0f}')

evenSquare()