# 1074-evenOrOdd.py
# Problem: Even or Odd
# Link: https://judge.beecrowd.com/en/problems/view/1074
# Solved on: 2024-08-20

def evenOrOdd():
    n = int(input())
    for _ in range(0, n):
        value = int(input())
        if value == 0:
            print('NULL')
        elif value % 2 == 0:
            if value > 0:
                print('EVEN POSITIVE')
            else:
                print('EVEN NEGATIVE')
        else:
            if value > 0:
                print('ODD POSITIVE')
            else:
                print('ODD NEGATIVE')

evenOrOdd()