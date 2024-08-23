# 1172-arrayReplacement1.py
# Problem: Array Replacement 1
# Link: https://judge.beecrowd.com/en/problems/view/1172
# Solved on: 2024-08-22

def arrayReplacement1():
    x = [0] * 10
    for i in range(10):
        x[i] = int(input())
        
    for i in range(10):
        if x[i] < 1:
            x[i] = 1
        print(f'X[{i}] = {x[i]}')
    
arrayReplacement1()