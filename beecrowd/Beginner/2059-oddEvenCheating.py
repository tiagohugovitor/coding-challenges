# 2057-oddEvenCheating.py
# Problem: Odd, Even or Cheating
# Link: https://judge.beecrowd.com/en/problems/view/2059
# Solved on: 2024-08-28

def oddEvenCheating():
    player1, number1, number2, cheating, accusing = map(int, input().split())
    if accusing or cheating:
        if accusing == 1:
            winner = 'Jogador 2 ganha!' if cheating == 1 else 'Jogador 1 ganha!'
        else:
            winner = 'Jogador 1 ganha!'
    else:
        total = (number1 + number2) % 2
        winner = 'Jogador 2 ganha!' if player1 == total else 'Jogador 1 ganha!'

    print(winner)
oddEvenCheating()
