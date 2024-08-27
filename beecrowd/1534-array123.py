# 1534-array123.py
# Problem: Array 123
# Link: https://judge.beecrowd.com/en/problems/view/1534
# Solved on: 2024-08-25

def array123():

    while True:
        try:
            n = int(input())
            for i in range(n):
                for j in range(n):
                    value = 3
                    if i + j == n - 1:
                        value = 2
                    elif i == j:
                        value = 1
                    print(f'{value}', end='')
                print('\n', end='')
        except EOFError:
            break

array123()