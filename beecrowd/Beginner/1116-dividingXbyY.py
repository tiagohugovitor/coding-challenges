# 1116-dividingXbyY.py
# Problem: Dividing X by Y
# Link: https://judge.beecrowd.com/en/problems/view/1116
# Solved on: 2024-08-21

def dividingXbyY():
    n = int(input())

    for _ in range(n):
        x, y = map(int, input().split())
        if y == 0:
            print('divisao impossivel')
        else:
            print(f'{(x/y):.1f}')

dividingXbyY()
