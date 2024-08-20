# 1050-ddd.py
# Problem: DDD
# Link: https://judge.beecrowd.com/en/problems/view/1050
# Solved on: 2024-08-19

def ddd():
    code = int(input())
    
    destinations = {
        61: 'Brasilia',
        71: 'Salvador',
        11: 'Sao Paulo',
        21: 'Rio de Janeiro',
        32: 'Juiz de Fora',
        19: 'Campinas',
        27: 'Vitoria',
        31: 'Belo Horizonte',
    }

    result = destinations[code] if code in destinations else 'DDD nao cadastrado'

    print(f'{result}')

ddd()