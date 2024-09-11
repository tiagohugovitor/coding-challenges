# 2147-galopeira.py
# Problem: Galopeira
# Link: https://judge.beecrowd.com/en/problems/view/2147
# Solved on: 2024-08-29

def galopeira():
    tests = int(input())
    for _ in range(tests):
        word = input()
        size = len(word)
        time = size/100

        print(f'{time:.2f}')
galopeira()
