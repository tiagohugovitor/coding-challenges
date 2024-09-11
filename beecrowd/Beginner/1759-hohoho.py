# 1759-hohoho.py
# Problem: Ho Ho Ho
# Link: https://judge.beecrowd.com/en/problems/view/1759
# Solved on: 2024-08-25

def hohoho():
    amount = int(input())
    for i in range(amount):
        print('Ho', end='')
        if i != amount - 1:
            print(' ', end='')
    print('!')

hohoho()