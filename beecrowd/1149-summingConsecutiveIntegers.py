# 1149-summingConsecutiveIntegers.py
# Problem: Summing Consecutive Integers
# Link: https://judge.beecrowd.com/en/problems/view/1149
# Solved on: 2024-08-22

def summingConsecutiveIntegers():
    values = input().split()
    a = int(values[0])
    for i in range(1, len(values)):
        if int(values[i]) > 0:
            n = int(values[i])
            break
    sum = 0
    for i in range(a, a+n):
        sum += i
    print(f'{sum}')

summingConsecutiveIntegers()
