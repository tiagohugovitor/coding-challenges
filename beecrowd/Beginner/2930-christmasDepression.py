# 2930-christmasDepression.py
# Problem: Final Thesis of Christmas Depression
# Link: https://judge.beecrowd.com/en/problems/view/2930
# Solved on: 2024-10-17

def christmasDepression():
    e, d = map(int, input().split())

    if e > d:
        print('Eu odeio a professora!')
        return

    if d - e >= 3:
        print('Muito bem! Apresenta antes do Natal!')
        return
    
    print('Parece o trabalho do meu filho!')

    if e + 2 < 24:
        print('TCC Apresentado!')
    
    else:
        print('Fail! Entao eh nataaaaal!')

christmasDepression()
