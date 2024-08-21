# 1115-quadrant.py
# Problem: Quadrant
# Link: https://judge.beecrowd.com/en/problems/view/1115
# Solved on: 2024-08-21

def quadrant():
    x, y = map(int, input().split())

    while x != 0 and y != 0:
        if x > 0:
            if y > 0:
                print('primeiro')
            else:
                print('quarto')
        else:
            if y > 0:
                print('segundo')
            else:
                print('terceiro')
            
        x, y = map(int, input().split())

quadrant()
