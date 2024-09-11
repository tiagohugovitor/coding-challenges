# 1072-interval2.py
# Problem: Interval 2
# Link: https://judge.beecrowd.com/en/problems/view/1072
# Solved on: 2024-08-19

def interval2():
    n = int(input())
    count = 0

    for _ in range(0, n):
        x = int(input())
        if x >= 10 and x <= 20:
            count += 1

    
    print(f'{count} in')
    print(f'{n - count} out')

interval2()