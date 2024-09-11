# 1183-aboveMainDiagonal.py
# Problem: Above the Main Diagonal
# Link: https://judge.beecrowd.com/en/problems/view/1183
# Solved on: 2024-08-24

def aboveMainDiagonal():
    operation  = input()
    m = [0] * 12
    for i in range(12):
        m[i] = [0] * 12

    for i in range(12):
        for j in range(12):
            m[i][j] = float(input())
    
    sum = 0
    for i in range(0, 12):
        for j in range(i + 1, 12):
            sum += m[i][j]
    
    result = sum if operation == 'S' else sum/66

    print(f'{result:.1f}')

aboveMainDiagonal()