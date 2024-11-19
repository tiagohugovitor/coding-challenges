# 1240-fitOrDontFit1.py
# Problem: Fit or Dont Fit 1
# Link: https://judge.beecrowd.com/en/problems/view/1240
# Solved on: 2024-11-18

def fitOrDontFit1():
    tests = int(input())

    for _ in range(tests):
        greater, smaller = map(int, input().split())

        if smaller > greater:
            print('nao encaixa')
            continue

        size = len(str(smaller))
        exp = pow(10, size)

        if greater % exp == smaller:
            print('encaixa')
        else:
            print('nao encaixa')

fitOrDontFit1()
