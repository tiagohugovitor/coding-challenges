# 1564-brazilWorldCup.py
# Problem: Brazil World Cup
# Link: https://judge.beecrowd.com/en/problems/view/1564
# Solved on: 2024-08-25

def brazilWorldCup():
    while True:
        try:
            n = int(input())
            result = 'copa' if n == 0 else 'duas'
            print(f'vai ter {result}!')
        except EOFError:
            break
brazilWorldCup()