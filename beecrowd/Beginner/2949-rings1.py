# 2949-rings1.py
# Problem: The Fellowship of the Ring
# Link: https://judge.beecrowd.com/en/problems/view/2949
# Solved on: 2024-10-16

def rings():
    people = int(input())
    count = {
        'X': 0,
        'H': 0,
        'E': 0,
        'A': 0,
        'M': 0,
    }

    species = {
        'X': 'Hobbit(s)',
        'A': 'Anao(oes)',
        'E': 'Elfo(s)',
        'H': 'Humano(s)',
        'M': 'Mago(s)',
    }

    for _ in range(people):
       _, type = input().split()
       count[type] += 1

    for total in count:
        print(f'{count[total]} {species[total]}')


rings()
