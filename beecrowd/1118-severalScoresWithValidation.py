# 1118-severalScoresWithValidation.py
# Problem: Several Scores with Validation
# Link: https://judge.beecrowd.com/en/problems/view/1118
# Solved on: 2024-08-21

def severalScoresWithValidation():
    option = 1
    while option != 2:
        firstScore = float(input())

        while firstScore < 0 or firstScore > 10:
            print('nota invalida')
            firstScore = float(input())

        secondScore = float(input())

        while secondScore < 0 or secondScore > 10:
            print('nota invalida')
            secondScore = float(input())

        print(f'media = {((secondScore + firstScore)/2):.2f}')
        print(f'novo calculo (1-sim 2-nao)')
        
        option = int(input())
        while option != 1 and option != 2:
            print(f'novo calculo (1-sim 2-nao)')
            option = int(input())

severalScoresWithValidation()
