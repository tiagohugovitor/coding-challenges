# 1153-simpleFactorial.py
# Problem: Simple Factorial
# Link: https://judge.beecrowd.com/en/problems/view/1153
# Solved on: 2024-08-22

def simpleFactorial():
    n = int(input())
    
    def factorial(x):
        if x == 0:
            return 1
        return x * factorial(x-1)
    
    print(f'{factorial(n)}')

simpleFactorial()