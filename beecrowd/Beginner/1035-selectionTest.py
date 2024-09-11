# 1035-selectionTest.py
# Problem: Selection Test
# Link: https://judge.beecrowd.com/en/problems/view/1035
# Solved on: 2024-08-18

def selectionTest():
    a, b, c, d = map(int, input().split())
    if b > c and d > a and (c+d) > (a+b) and c >= 0 and d >= 0 and a % 2 == 0:
        print('Valores aceitos')
    else:
        print('Valores nao aceitos') 

selectionTest()