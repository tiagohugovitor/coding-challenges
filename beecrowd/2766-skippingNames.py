# 2766-skippingNames.py
# Problem: Input and Output Reading and Skipping Names
# Link: https://judge.beecrowd.com/en/problems/view/2766
# Solved on: 2024-09-10

def skippingNames():
    while True:
        try:
            names = [0] * 10
            for i in range(10):
                names[i] = input()

            print(f'{names[2]}')
            print(f'{names[6]}')
            print(f'{names[8]}')

        except EOFError:
            break

skippingNames()
