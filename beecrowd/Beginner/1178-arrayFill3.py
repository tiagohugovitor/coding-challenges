# 1178-arrayFill3.py
# Problem: Array Fill 3
# Link: https://judge.beecrowd.com/en/problems/view/1178
# Solved on: 2024-08-22

def arrayFill3():
    n = [0] * 100
    first = float(input())
    n[0] = first
    for i in range(1, 100):
        n[i] = n[i-1]/2

    for i in range(0, 100):
        print(f'N[{i}] = {n[i]:.4f}') 

arrayFill3()