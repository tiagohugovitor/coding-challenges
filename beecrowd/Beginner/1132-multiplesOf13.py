# 1132-multiplesOf13.py
# Problem: Multiples of 13
# Link: https://judge.beecrowd.com/en/problems/view/1132
# Solved on: 2024-08-21

def multiplesOf13():
    x = int(input())
    y = int(input())

    if y < x:
        x, y = y, x

    sum = 0
    for i in range(x, y + 1):
        if i % 13 != 0:
            sum += i
    print(f'{sum}')

multiplesOf13()
