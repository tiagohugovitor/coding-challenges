# 2221-pokemonsBattle.py
# Problem: Pokemons Battle
# Link: https://judge.beecrowd.com/en/problems/view/2221
# Solved on: 2024-09-02

def pokemonsBattle():
    tests = int(input())
    for _ in range(tests):
        bonus = int(input())
        dabrielAttack, dabrielDefense, dabrielLevel = map(int, input().split())
        guarteAttack, guarteDefense, guarteLevel = map(int, input().split())
        
        dabrielBonus = bonus if dabrielLevel % 2 == 0 else 0
        totalDabriel = (dabrielAttack + dabrielDefense)/2 + dabrielBonus

        guarteBonus = bonus if guarteLevel % 2 == 0 else 0
        totalGuarte = (guarteAttack + guarteDefense) / 2 + guarteBonus

        if totalDabriel > totalGuarte:
            print('Dabriel')
        elif totalGuarte > totalDabriel:
            print('Guarte')
        else:
            print('Empate')

pokemonsBattle()
