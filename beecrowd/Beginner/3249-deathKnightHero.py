# 3249-deathKnightHero.py
# Problem: Death Knight Hero
# Link: https://judge.beecrowd.com/en/problems/view/3249
# Solved on: 2024-10-30

def deathKnightHero():
    battles = int(input())
    battlesWon = 0

    for _ in range(battles):
        abilities = input()
        if 'CD' not in abilities:
            battlesWon += 1

    print(battlesWon)

deathKnightHero()
