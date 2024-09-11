# 2630-greyscale.py
# Problem: Greyscale
# Link: https://judge.beecrowd.com/en/problems/view/2630
# Solved on: 2024-09-05

def greyscale():
    tests = int(input())
    for case in range(tests):
        operation = input()
        r, g, b = map(int, input().split())

        if operation == 'eye':
            p = 0.3 * r + 0.59 * g + 0.11 * b
        
        elif operation == 'mean':
            p = (r + g + b) / 3

        elif operation == 'max':
            p = max(r, g, b)
        
        else:
            p = min(r, g, b)

        print(f'Caso #{case + 1}: {int(p)}')

greyscale()
