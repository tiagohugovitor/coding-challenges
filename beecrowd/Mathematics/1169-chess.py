# 1169-chess.py
# Problem: Grains in a Chess Board
# Link: https://judge.beecrowd.com/en/problems/view/1169
# Solved on: 2024-11-18

def chess():
    tests = int(input())

    for _ in range(tests):
        squares = int(input())
        total = pow(2, squares) - 1

        total /= 12000

        print(f'{int(total)} kg')

chess()
