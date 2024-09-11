# 1174-arraySelection1.py
# Problem: Array Selection 1
# Link: https://judge.beecrowd.com/en/problems/view/1174
# Solved on: 2024-08-22

def arraySelection1():
    a = [0] * 100
    
    for i in range(0, 100):
        a[i] = float(input())

        if a[i] <= 10:
            print(f'A[{i}] = {a[i]}')

arraySelection1()