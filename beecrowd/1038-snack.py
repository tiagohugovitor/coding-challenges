# 1038-snack.py
# Problem: Snack
# Link: https://judge.beecrowd.com/en/problems/view/1038
# Solved on: 2024-08-18

def snack():

    prices = [4, 4.5, 5, 2, 1.5]
    id, amount = map(int, input().split())
    total = amount * prices[id-1]
    print(f'Total: R$ {total:.2f}')

snack()