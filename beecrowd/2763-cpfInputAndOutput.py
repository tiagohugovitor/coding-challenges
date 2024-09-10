# 2763-cpfInputAndOutput.py
# Problem: CPF Input and Output
# Link: https://judge.beecrowd.com/en/problems/view/2763
# Solved on: 2024-09-10

def cpfInputAndOutput():
    while True:
        try:
            a, b, c = input().split('.')
            c, d = c.split('-')

            print(a)
            print(b)
            print(c)
            print(d)

        except EOFError:
            break

cpfInputAndOutput()
