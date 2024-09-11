# 1865-mjolnir.py
# Problem: Mjölnir
# Link: https://judge.beecrowd.com/en/problems/view/1865
# Solved on: 2024-08-27

def mjolnir():
    tests = int(input())
    for _ in range(tests):
        character = input().split()
        if character[0] == 'Thor':
            print('Y')
        else:
            print('N')

mjolnir()
