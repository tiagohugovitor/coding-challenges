# 1101-sequenceOfNumbersAndSum.py
# Problem: Sequence of Numbers and Sum
# Link: https://judge.beecrowd.com/en/problems/view/1101
# Solved on: 2024-08-20

def sequenceOfNumbersAndSum():
    m, n = map(int, input().split())

    while m > 0 and n > 0:
        if m > n:
            m, n = n, m
        sum = 0
        for i in range(m, n+1):
            print(f'{i} ', end='')
            sum += i
        print(f'Sum={sum}')
        m, n = map(int, input().split())

sequenceOfNumbersAndSum()
