# 1165-primeNumber.py
# Problem: Prime Number
# Link: https://judge.beecrowd.com/en/problems/view/1165
# Solved on: 2024-08-22

def primeNumber():
    tests = int(input())
    for _ in range(tests):
        number = int(input())
        isPrime = True
        for i in range(2, (number//2) + 1):
            if number % i == 0:
                isPrime = False
                break

        if isPrime:
            print(f'{number} eh primo')
        
        else:
            print(f'{number} nao eh primo')

primeNumber()