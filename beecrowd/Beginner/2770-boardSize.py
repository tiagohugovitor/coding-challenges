# 2770-boardSize.py
# Problem: Board Size
# Link: https://judge.beecrowd.com/en/problems/view/2770
# Solved on: 2024-09-11

import sys

def boardSize():
    input = sys.stdin.read
    data = input().splitlines()
    i = 0
    while i < len(data):
        x, y, m = map(int, data[i].split())
        i += 1
        for _ in range(m):
            orderX, orderY = map(int, data[i].split())
            i += 1
            if (orderY <= y and orderX <= x) or (orderY <= x and orderX <= y):
                sys.stdout.write('Sim\n')
            else:
                sys.stdout.write('Nao\n')

boardSize()
