# 1177-arrayFill2.py
# Problem: Array Fill 2
# Link: https://judge.beecrowd.com/en/problems/view/1177
# Solved on: 2024-08-22

def arrayFill2():
    n = [0] * 1000
    maximumValue = int(input())
    current = 0
    for i in range(0, 1000):
        n[i] = current
        current += 1
        if current == maximumValue:
            current = 0

    for i in range(0, 1000):
        print(f'N[{i}] = {n[i]}') 

arrayFill2()