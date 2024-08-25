# 1187-topArea.py
# Problem: Top Area
# Link: https://judge.beecrowd.com/en/problems/view/1187
# Solved on: 2024-08-24

def topArea():
    operation  = input()
    m = [0] * 12
    for i in range(12):
        m[i] = [0] * 12

    for i in range(12):
        for j in range(12):
            m[i][j] = float(input())
    
    sum = 0
    for i in range(0, 5):
        for j in range(i + 1, 11 - i):
            sum += m[i][j]
    
    result = sum if operation == 'S' else sum/30

    print(f'{result:.1f}')

topArea()