# 1010-simpleCalculate.py
# Problem: Simple Calculate
# Link: https://judge.beecrowd.com/en/problems/view/1010
# Solved on: 2024-08-18

def simpleCalculate():
    firstProduct = input().split()
    secondProduct = input().split()
    total = (int(firstProduct[1]) * float(firstProduct[2])) + (int(secondProduct[1]) * float(secondProduct[2]))
    print(f'VALOR A PAGAR: R$ {total:.2f}')

simpleCalculate()