# 2764-dateInputOutput.py
# Problem: Date Input and Output
# Link: https://judge.beecrowd.com/en/problems/view/2764
# Solved on: 2024-09-10

def dateInputOutput():
    while True:
        try:
            a, b, c = input().split('/')

            print(f'{b}/{a}/{c}')
            print(f'{c}/{b}/{a}')
            print(f'{a}-{b}-{c}')

        except EOFError:
            break

dateInputOutput()
