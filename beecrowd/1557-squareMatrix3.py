# 1557-squareMatrix3.py
# Problem: Square Matrix 3
# Link: https://judge.beecrowd.com/en/problems/view/1557
# Solved on: 2024-08-25

def squareMatrix3():
    while True:
        n = int(input())
        if n == 0:
            break
        t = len(str(pow(2, 2*n - 2)))
        for i in range(n):
            for j in range(n):
                value = pow(2, i+j)
                print(f'{value:>{t}}', end='')
                if j != n - 1:
                    print(' ', end='') 
            print()
        print()

squareMatrix3()