# 1181-lineInArray.py
# Problem: Line in Array
# Link: https://judge.beecrowd.com/en/problems/view/1181
# Solved on: 2024-08-22

def lineInArray():
    line = int(input())
    operation  = input()
    m = [0] * 12
    for i in range(12):
        m[i] = [0] * 12

    for i in range(12):
        for j in range(12):
            m[i][j] = float(input())
    
    sum = 0
    for i in range(12):
        sum += m[line][i]
    
    result = sum if operation == 'S' else sum/12

    print(f'{result:.1f}')

lineInArray()