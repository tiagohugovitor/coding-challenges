# 1041-coordinatesOfPoint.py
# Problem: Coordinates of a Point
# Link: https://judge.beecrowd.com/en/problems/view/1041
# Solved on: 2024-08-19

def coordinatesOfPoint():

    x, y = map(float, input().split())

    if x == 0.0 and y == 0.0:
        print('Origem')
        return
    
    if x == 0:
        print('Eixo Y')
        return
    
    if y == 0:
        print('Eixo X')
        return
    
    if x > 0:
        if y > 0:
            print('Q1')
        else:
            print('Q4')
    else:
        if y > 0:
            print('Q2')
        else:
            print('Q3')

coordinatesOfPoint()