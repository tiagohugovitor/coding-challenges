# 2765-comingInputOutput.py
# Problem: Coming Input and Output
# Link: https://judge.beecrowd.com/en/problems/view/2765
# Solved on: 2024-09-10

def comingInputOutput():
    while True:
        try:
            a, b = input().split(',')

            print(f'{a}')
            print(f'{b}')

        except EOFError:
            break

comingInputOutput()
