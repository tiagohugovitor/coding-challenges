# 2544-kageBunshinNoJutsu.py
# Problem: Kage Bunshin no Jutsu
# Link: https://judge.beecrowd.com/en/problems/view/2544
# Solved on: 2024-09-05

def clones(ninjas, technique):
    if ninjas == 1:
        return technique
    return clones(ninjas / 2, technique + 1)

def kageBunshinNoJutsu():
    while True:
        try:
            amount = int(input())
            response = clones(amount, 0)

            print(response)

        except EOFError:
            break

kageBunshinNoJutsu()
