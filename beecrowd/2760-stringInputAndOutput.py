# 2760-stringInputAndOutput.py
# Problem: String Input and Output
# Link: https://judge.beecrowd.com/en/problems/view/2760
# Solved on: 2024-09-10

def stringInputAndOutput():
    while True:
        try:
            a = input()
            b = input()
            c = input()

            print(f'{a}{b}{c}')
            print(f'{b}{c}{a}')
            print(f'{c}{a}{b}')
            print(f'{a[:10]}{b[:10]}{c[:10]}')

        except EOFError:
            break

stringInputAndOutput()
