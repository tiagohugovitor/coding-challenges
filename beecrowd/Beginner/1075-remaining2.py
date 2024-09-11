# 1075-remaining2.py
# Problem: Remaining 2
# Link: https://judge.beecrowd.com/en/problems/view/1075
# Solved on: 2024-08-20

def remaining2():
    n = int(input())

    if n > 2:
        print('2')
    
    for i in range(n+1, 10000):
        if i % n == 2:
            print(f'{i}')

remaining2()