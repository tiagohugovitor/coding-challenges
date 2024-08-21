# 1078-multiplicationTable.py
# Problem: Multiplication Table
# Link: https://judge.beecrowd.com/en/problems/view/1078
# Solved on: 2024-08-20

def multiplicationTable():
    n = int(input())
    
    for i in range(1, 11):
        print(f'{i} x {n} = {i*n}')

multiplicationTable()