# 3342-keanu.py
# Problem: Keanu
# Link: https://judge.beecrowd.com/en/problems/view/3342
# Solved on: 2024-09-03

def keanu():
    n = int(input())

    if n % 2 == 0:
        white = (n/2) * n
        black = white
    else:
        white = ((n - 1) /2) * (n - 1) + n 
        black = white - 1

    print(f'{int(white)} casas brancas e {int(black)} casas pretas')

keanu()