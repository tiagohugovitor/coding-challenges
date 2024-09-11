# 2031-rockPaperAirstrike.py
# Problem: Rock, Paper, Airstrike
# Link: https://judge.beecrowd.com/en/problems/view/2031
# Solved on: 2024-08-28

def rockPaperAirstrike():
    losesTo = {
        'pedra': ['ataque'],
        'papel': ['pedra', 'ataque'],
        'ataque': [],
    }
    ties = {
        'pedra': 'Sem ganhador',
        'papel': 'Ambos venceram',
        'ataque': 'Aniquilacao mutua',
    }
    tests = int(input())

    for _ in range(tests):
        firstPlayer = input()
        secondPlayer = input()

        if firstPlayer == secondPlayer:
            print(ties[firstPlayer])
        elif secondPlayer in losesTo[firstPlayer]:
            print('Jogador 2 venceu')
        else:
            print('Jogador 1 venceu')

rockPaperAirstrike()
