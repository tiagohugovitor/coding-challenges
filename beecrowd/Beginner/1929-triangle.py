# 1929-triangle.py
# Problem: Triangle
# Link: https://judge.beecrowd.com/en/problems/view/1929
# Solved on: 2024-08-27

def triangle():
    a, b, c, d = map(int, input().split())
    if ((a < b + c and b < c + a and c < b + a) or
        (a < b + d and b < a + d and d < a + b) or
        (a < c + d and c < a + d and d < a + c) or
        (c < b + d and b < c + d and d < c + b)):
        print('S')
    else:
        print('N')
    
triangle()

def simplifiedTriangle():
    a, b, c, d = sorted(map(int, input().split()))
    
    if a + b > c or b + c > d:
        print('S')
    else:
        print('N')

