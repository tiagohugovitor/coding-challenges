# 2313-whichTriangle.py
# Problem: Which Triangle
# Link: https://judge.beecrowd.com/en/problems/view/2313
# Solved on: 2024-09-04

def whichTriangle():
    a, b, c = map(int, input().split())

    if a >= b + c or b >= a + c or c >= a + b:
        print('Invalido')
        return

    if a == b and b == c:
        print('Valido-Equilatero')

    elif a == b or b == c or a == c:
        print('Valido-Isoceles')
    
    else:
        print('Valido-Escaleno')

    ordered = [a, b, c]
    ordered.sort()

    if pow(ordered[2], 2) == (pow(ordered[1], 2) + pow(ordered[0], 2)):
        print('Retangulo: S')
    else:
        print('Retangulo: N')

whichTriangle()
