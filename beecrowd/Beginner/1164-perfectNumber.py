# 1164-perfectNumber.py
# Problem: Perfect Number
# Link: https://judge.beecrowd.com/en/problems/view/1164
# Solved on: 2024-08-22

def perfectNumber():
    tests = int(input())
    for _ in range(tests):
        number = int(input())
        sum = 0
        for i in range(1, (number//2) + 1):
            if number % i == 0:
                sum += i 

        if sum == number:
            print(f'{number} eh perfeito')
        
        else:
            print(f'{number} nao eh perfeito')

perfectNumber()