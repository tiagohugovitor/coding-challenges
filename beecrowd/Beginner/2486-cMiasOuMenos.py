# 2486-cMaisOuMenos.py
# Problem: C Mais Ou Menos?
# Link: https://judge.beecrowd.com/en/problems/view/2486
# Solved on: 2024-09-04

def cMaisOuMenos():
    vitaminC = {
        'suco de laranja': 120,
        'morango fresco': 85,
        'mamao': 85,
        'goiaba vermelha': 70,
        'manga': 56,
        'laranja': 50,
        'brocolis': 34,
    }
    while True:
        products = int(input())
        
        if products == 0:
            break
        sum = 0
        for _ in range(products):
            amount, product = input().split(' ', 1)
            amount = int(amount)
            sum += (vitaminC[product] * amount)

        if sum > 130:
            print(f'Menos {sum - 130} mg')
        
        elif sum < 110:
            print(f'Mais {110 - sum} mg')
        
        else:
            print(f'{sum} mg')

cMaisOuMenos()
