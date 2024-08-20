# 1043-triangle.py
# Problem: Triangle
# Link: https://judge.beecrowd.com/en/problems/view/1043
# Solved on: 2024-08-19

def triangle():

    a, b, c = map(float, input().split())

    if a < b + c and b < a + c and c < a + b:
        perimeter = a + b + c
        print(f'Perimetro = {perimeter:.1f}')
    else:
        area = (a + b) * c / 2
        print(f'Area = {area:.1f}')

triangle()