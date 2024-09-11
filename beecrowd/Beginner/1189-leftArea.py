# 1189-leftArea.py
# Problem: Left Area
# Link: https://judge.beecrowd.com/en/problems/view/1189
# Solved on: 2024-08-24

def leftArea():
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
            sum += m[j][i]
    
    result = sum if operation == 'S' else sum/30

    print(f'{result:.1f}')

leftArea()