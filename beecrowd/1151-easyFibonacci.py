# 1151-easyFibonacci.py
# Problem: Easy Fibonacci
# Link: https://judge.beecrowd.com/en/problems/view/1151
# Solved on: 2024-08-22

def easyFibonacci():
    n = int(input())

    if n == 1:
        print('0')
        return

    if n == 2:
        print('0 1')
        return
    
    previous = 0
    current = 1

    print('0 1', end='')
    count = 2
    while count < n:
        next = current + previous
        print(f' {next}', end='')
        previous = current
        current = next
        count += 1
    
    print('')

easyFibonacci()