# 1873-rockPaperScissors.py
# Problem: Rock-paper-scissors-lizard-spock
# Link: https://judge.beecrowd.com/en/problems/view/1873
# Solved on: 2024-11-04

def rockPaperScissors():
    tests = int(input())

    losesTo = {
        'pedra': ['papel', 'spock'],
        'papel': ['tesoura', 'lagarto'],
        'tesoura': ['spock', 'pedra'],
        'lagarto': ['pedra', 'tesoura'],
        'spock' : ['lagarto', 'papel'],
    }

    for _ in range(tests):
        rajesh, sheldon = input().split()

        if rajesh == sheldon:
            print('empate')
            continue
            
        if sheldon in losesTo[rajesh]:
            print('sheldon')
            continue

        print('rajesh')

rockPaperScissors()