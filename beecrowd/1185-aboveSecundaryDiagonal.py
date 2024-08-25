# 1185-aboveSecundaryDiagonal.py
# Problem: Above the Secundary Diagonal
# Link: https://judge.beecrowd.com/en/problems/view/1185
# Solved on: 2024-08-24

def aboveSecundaryDiagonal():
    operation  = input()
    m = [0] * 12
    for i in range(12):
        m[i] = [0] * 12

    for i in range(12):
        for j in range(12):
            m[i][j] = float(input())
    
    sum = 0
    for i in range(0, 12):
        for j in range(0, 11 - i):
            sum += m[i][j]
    
    result = sum if operation == 'S' else sum/66

    print(f'{result:.1f}')

aboveSecundaryDiagonal()