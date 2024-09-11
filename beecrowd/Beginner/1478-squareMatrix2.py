# 1478-squareMatrix2.py
# Problem: Square Matrix 2
# Link: https://judge.beecrowd.com/en/problems/view/1478
# Solved on: 2024-08-25

def squareMatrix2():

    n = int(input())
    while n != 0:
        for i in range(n):
            for j in range(n):
                value = abs(i - j) + 1
                print(f'{value:>3}', end='')
                if j != n - 1:
                    print(' ', end='')
            print('\n', end='')
        print('\n', end = '')
        n = int(input())

squareMatrix2()