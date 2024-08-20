# 1044-multiples.py
# Problem: Multiples
# Link: https://judge.beecrowd.com/en/problems/view/1044
# Solved on: 2024-08-19

def multiples():

    a, b = map(int, input().split())

    if a % b == 0 or b % a == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')

multiples()