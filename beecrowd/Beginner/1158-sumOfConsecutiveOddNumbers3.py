# 1158-sumOfConsecutiveOddNumbers3.py
# Problem: Sum of Consecutive Odd Numbers III
# Link: https://judge.beecrowd.com/en/problems/view/1158
# Solved on: 2024-08-22

def sumOfConsecutiveOddNumbers3():
    n = int(input())
    for _ in range(n):
        x, y = map(int, input().split())

        x = x + 1 if x % 2 == 0 else x
        sum = x
        count = 1

        while count < y:
            x = x + 2
            sum += x
            count += 1

        print(f'{sum}')

sumOfConsecutiveOddNumbers3()