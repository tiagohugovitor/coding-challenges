# 1182-columnInArray.py
# Problem: Column in Array
# Link: https://judge.beecrowd.com/en/problems/view/1182
# Solved on: 2024-08-24

def columnInArray():
    column = int(input())
    operation  = input()
    m = [0] * 12
    for i in range(12):
        m[i] = [0] * 12

    for i in range(12):
        for j in range(12):
            m[i][j] = float(input())
    
    sum = 0
    for i in range(12):
        sum += m[i][column]
    
    result = sum if operation == 'S' else sum/12

    print(f'{result:.1f}')

columnInArray()