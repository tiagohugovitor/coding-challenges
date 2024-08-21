# 1131-grenais.py
# Problem: Grenais
# Link: https://judge.beecrowd.com/en/problems/view/1131
# Solved on: 2024-08-21

def grenais():
    inter = 0
    gremio = 0
    ties = 0
    while True:
        interGoals,gremioGoals = map(int, input().split())
        if interGoals > gremioGoals:
            inter += 1
        elif gremioGoals > interGoals:
            gremio += 1
        else:
            ties += 1
        
        option = 0
        while option not in [1, 2]:
            print('Novo grenal (1-sim 2-nao)')
            option = int(input())
        if option == 2:
            break
    print(f'{inter + gremio + ties} grenais')
    print(f'Inter:{inter}')
    print(f'Gremio:{gremio}')
    print(f'Empates:{ties}')
    if inter == gremio:
        print('Nao houve vencedor')
    else:
        winner = 'Gremio' if gremio > inter else 'Inter'
        print(f'{winner} venceu mais')

grenais()
