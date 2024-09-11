# 2757-inputAndOutputOfIntegers.py
# Problem: Input and Output of Integers
# Link: https://judge.beecrowd.com/en/problems/view/2757
# Solved on: 2024-09-10

def inputAndOutputOfIntegers():
    while True:
        try:
            a = int(input())
            b = int(input())
            c = int(input())

            aStr = f'{abs(a):0>9}' if a < 0 else f'{a:0>10}'
            aStr = f'-{aStr}' if a < 0 else aStr

            print(f'A = {a}, B = {b}, C = {c}')
            print(f'A = {a:>10}, B = {b:>10}, C = {c:>10}')
            print(f'A = {aStr}, B = {b:0>10}, C = {c:0>10}')
            print(f'A = {a:<10}, B = {b:<10}, C = {c:<10}')
        except EOFError:
            break

inputAndOutputOfIntegers()
