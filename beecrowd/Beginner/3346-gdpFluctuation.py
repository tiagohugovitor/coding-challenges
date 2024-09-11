# 3346-gdpFluctuation.py
# Problem: GDP Fluctuation
# Link: https://judge.beecrowd.com/en/problems/view/3346
# Solved on: 2024-09-03

def gdpFluctuation():
    f1, f2 = map(float, input().split())
    result = (((1 + f1/100) * (1 + f2/100)) - 1) * 100

    print(f'{result:.6f}')

gdpFluctuation()