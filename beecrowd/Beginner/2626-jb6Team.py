# 2626-jb6Team.py
# Problem: JB6 Team
# Link: https://judge.beecrowd.com/en/problems/view/2626
# Solved on: 2024-09-05

def jb6Team():
    losesTo = {
        'papel': 'tesoura',
        'tesoura': 'pedra',
        'pedra': 'papel',
    }

    while True:
        try:
            dodo, leo, pepper = input().split()

            if dodo == leo == pepper:
                print('Putz vei, o Leo ta demorando muito pra jogar...')
                continue
        
            winCount = {
                'dodo': (dodo == losesTo[leo]) + (dodo == losesTo[pepper]),
                'leo': (leo == losesTo[dodo]) + (leo == losesTo[pepper]),
                'pepper': (pepper == losesTo[dodo]) + (pepper == losesTo[leo]),
            }

            if winCount['dodo'] == 2:
                print('Os atributos dos monstros vao ser inteligencia, sabedoria...')
            elif winCount['leo'] == 2:
                print("Iron Maiden's gonna get you, no matter how far!")
            elif winCount['pepper'] == 2:
                print('Urano perdeu algo muito precioso...')
            else:
                print('Putz vei, o Leo ta demorando muito pra jogar...')

        except EOFError:
            break

jb6Team()
