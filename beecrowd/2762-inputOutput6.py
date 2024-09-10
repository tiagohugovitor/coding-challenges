# 2762-inputOutput6.py
# Problem: Input and Output 6
# Link: https://judge.beecrowd.com/en/problems/view/2762
# Solved on: 2024-09-10

def inputOutput6():
    while True:
        try:
            a, b = input().split('.')
            b = int(b)
            print(f'{b}.{a}')

        except EOFError:
            break

inputOutput6()
