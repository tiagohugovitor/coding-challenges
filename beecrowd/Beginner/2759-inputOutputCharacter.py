# 2759-inputAndOutputCharacter.py
# Problem: Input and Output Character
# Link: https://judge.beecrowd.com/en/problems/view/2759
# Solved on: 2024-09-10

def inputAndOutputCharacter():
    while True:
        try:
            a = input()
            b = input()
            c = input()

            print(f'A = {a}, B = {b}, C = {c}')
            print(f'A = {b}, B = {c}, C = {a}')
            print(f'A = {c}, B = {a}, C = {b}')

        except EOFError:
            break

inputAndOutputCharacter()
