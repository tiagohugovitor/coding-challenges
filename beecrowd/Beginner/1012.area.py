# 1012-area.py
# Problem: Area
# Link: https://judge.beecrowd.com/en/problems/view/1012
# Solved on: 2024-08-18

def area():
    a, b, c = map(float, input().split())
    pi = 3.14159
    triangle = (a * c) / 2
    circle = c * c * pi
    trapezoid = (a + b) * c / 2
    square = b * b
    rectangle = a * b
    print(f'TRIANGULO: {triangle:.3f}')
    print(f'CIRCULO: {circle:.3f}')
    print(f'TRAPEZIO: {trapezoid:.3f}')
    print(f'QUADRADO: {square:.3f}')
    print(f'RETANGULO: {rectangle:.3f}')

area()