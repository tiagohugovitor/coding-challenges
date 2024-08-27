# 1828-bazinga.py
# Problem: Bazinga!
# Link: https://judge.beecrowd.com/en/problems/view/1828
# Solved on: 2024-08-26

def bazinga():
    losesTo = {
        'tesoura': ['Spock', 'pedra'],
        'papel': ['tesoura', 'lagarto'],
        'pedra': ['papel', 'Spock'],
        'lagarto': ['pedra', 'tesoura'],
        'Spock': ['lagarto', 'papel'],
    }
    tests = int(input())
    for i in range(tests):
        sheldon, raj = input().split()
        if sheldon == raj:
            result = 'De novo'
        else:
            result = 'Bazinga' if losesTo[raj].__contains__(sheldon) else 'Raj trapaceou'
        print(f'Caso #{i + 1}: {result}!')

bazinga()
