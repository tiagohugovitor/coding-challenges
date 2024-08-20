# 1066-evenOddPositiveNegative.py
# Problem: Even, Odd, Positive and Negative
# Link: https://judge.beecrowd.com/en/problems/view/1066
# Solved on: 2024-08-19

def evenOddPositiveNegative():
    even = 0
    odd = 0
    positive = 0
    negative = 0
    for _ in range(0, 5):
        value = float(input())
        if value % 2 == 0:
            even += 1
        else:
            odd += 1
        if value > 0:
            positive += 1
        if value < 0:
            negative += 1


    print(f'{even} valor(es) par(es)')
    print(f'{odd} valor(es) impar(es)')
    print(f'{positive} valor(es) positivo(s)')
    print(f'{negative} valor(es) negativo(s)')

evenOddPositiveNegative()