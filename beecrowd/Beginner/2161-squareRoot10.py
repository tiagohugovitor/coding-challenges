# 2161-squareRoot10.py
# Problem: Square Root of 10
# Link: https://judge.beecrowd.com/en/problems/view/2161
# Solved on: 2024-08-30

def squareRoot10():
    n = int(input())
    
    if n == 0:
        result = 3.0
    else: 
        result = 6
        for _ in range(n - 1):
            result = 6 + 1 / result
        
        result = 3 + 1 / result
    
    print(f"{result:.10f}")
squareRoot10()
