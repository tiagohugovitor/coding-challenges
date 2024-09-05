# 2310-volleyball.py
# Problem: Volleyball
# Link: https://judge.beecrowd.com/en/problems/view/2310
# Solved on: 2024-09-04

def volleyball():
    players = int(input())
    serviceAttempt = 0
    serviceSuccess = 0
    blockAttempt = 0
    blockSuccess = 0
    attackAttempt = 0
    attackSuccess = 0

    for _ in range(players):
        _ = input()
        sA, bA, aA = map(int, input().split())
        sS, bS, aS = map(int, input().split())
        serviceAttempt += sA
        serviceSuccess += sS
        blockAttempt += bA
        blockSuccess += bS
        attackAttempt += aA
        attackSuccess += aS

    servicePercentage = serviceSuccess * 100 / serviceAttempt
    blocksPercentage = blockSuccess * 100 / blockAttempt
    attackPercentage = attackSuccess * 100 / attackAttempt

    print(f'Pontos de Saque: {servicePercentage:.2f} %.')
    print(f'Pontos de Bloqueio: {blocksPercentage:.2f} %.')
    print(f'Pontos de Ataque: {attackPercentage:.2f} %.')

volleyball()
