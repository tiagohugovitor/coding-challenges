# 2747-output1.py
# Problem: Output 1
# Link: https://judge.beecrowd.com/en/problems/view/2747
# Solved on: 2024-09-06

def output1():
    for _ in range(39):
        print('-', end='')
    print()
    for _ in range(5):
        print('|', end='')
        for _ in range(37):
            print(' ', end='')
        print('|')
    for _ in range(39):
        print('-', end='')
    print()

output1()
