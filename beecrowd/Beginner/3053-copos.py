# 3053-copos.py
# Problem: Jogo dos Copos
# Link: https://judge.beecrowd.com/en/problems/view/3053
# Solved on: 2024-10-21

def copos():
    moves = int(input())
    choosenCup = input()

    for _ in range(moves):
        move = int(input())
        if move == 1:
            if choosenCup == 'A':
                choosenCup = 'B'
            elif choosenCup == 'B':
                choosenCup = 'A'
        if move == 2:
            if choosenCup == 'B':
                choosenCup = 'C'
            elif choosenCup == 'C':
                choosenCup = 'B'
        if move == 3:
            if choosenCup == 'A':
                choosenCup = 'C'
            elif choosenCup == 'C':
                choosenCup = 'A'

    print(choosenCup)

copos()
