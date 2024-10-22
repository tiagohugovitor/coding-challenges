# 3170-christmasBalls.py
# Problem: Christmas Balls
# Link: https://judge.beecrowd.com/en/problems/view/3170
# Solved on: 2024-10-21

def christmasBalls():
    balls = int(input())
    branches = int(input())

    neededBalls = branches // 2

    if neededBalls <= balls:
        print('Amelia tem todas bolinhas!')
    
    else:
        print(f'Faltam {neededBalls - balls} bolinha(s)')

christmasBalls()
