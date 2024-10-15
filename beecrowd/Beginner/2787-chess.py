# 2787-chess.py
# Problem: Chess
# Link: https://judge.beecrowd.com/en/problems/view/2787
# Solved on: 2024-10-14

def chess():
    lines = int(input())
    columns = int(input())
    
    if lines % 2 == columns % 2:
        print('1')
    else:
        print('0')


chess()
