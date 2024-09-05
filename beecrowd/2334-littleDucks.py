# 2334-littleDucks.py
# Problem: Little Ducks
# Link: https://judge.beecrowd.com/en/problems/view/2334
# Solved on: 2024-09-04

def littleDucks():
    while True:
        ducks = int(input())
        if ducks == -1:
            break
        if ducks == 0:
            print('0')
        else:
            print(ducks - 1)

littleDucks()
