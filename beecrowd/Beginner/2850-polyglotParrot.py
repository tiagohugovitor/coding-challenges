# 2850-polyglotParrot.py
# Problem: Polyglot Parrot
# Link: https://judge.beecrowd.com/en/problems/view/2850
# Solved on: 2024-10-21

def polyglotParrot():
    outputs = {
        'esquerda': 'ingles',
        'direita': 'frances',
        'nenhuma': 'portugues',
        'as duas': 'caiu'
    }

    while True:
        try:
            parrotLeg = input()
            print(outputs[parrotLeg])
        except EOFError:
            break
polyglotParrot()
