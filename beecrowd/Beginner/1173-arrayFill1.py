# 1173-arrayFill1.py
# Problem: Array Fill 1
# Link: https://judge.beecrowd.com/en/problems/view/1173
# Solved on: 2024-08-22

def arrayFill1():
    n = [0] * 10
    n[0] = int(input())
        
    for i in range(1, 10):
        n[i] = n[i - 1] * 2
    
    for i in range(10):
        print(f'N[{i}] = {n[i]}')
    
arrayFill1()