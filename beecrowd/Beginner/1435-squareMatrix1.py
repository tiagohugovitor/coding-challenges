# 1435-squareMatrix1.py
# Problem: Square Matrix 1
# Link: https://judge.beecrowd.com/en/problems/view/1435
# Solved on: 2024-08-25

def squareMatrix1():

    n = int(input())
    while n != 0:
        for i in range(n):
            for j in range(n):
                value = min(i + 1, j + 1 , n-i, n-j)
                print(f'{value:>3}', end='')
                if j != n - 1:
                    print(' ', end='')
            print('\n', end='')
        print('\n', end = '')
        n = int(input())

squareMatrix1()