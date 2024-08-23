# 1175-arrayChange1.py
# Problem: Array Change 1
# Link: https://judge.beecrowd.com/en/problems/view/1175
# Solved on: 2024-08-22

def arrayChange1():
    n = [0] * 20
    
    for i in range(0, 20):
        n[i] = int(input())

    for i in range(0, 10):
        temp = n[-(i + 1)]
        n[-(i + 1)] = n[i]
        n[i] = temp

    for i in range(0, 20):
        print(f'N[{i}] = {n[i]}')

arrayChange1()