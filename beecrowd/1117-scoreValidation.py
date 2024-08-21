# 1117-scoreValidation.py
# Problem: Score Validation
# Link: https://judge.beecrowd.com/en/problems/view/1117
# Solved on: 2024-08-21

def scoreValidation():
    firstScore = float(input())

    while firstScore < 0 or firstScore > 10:
        print('nota invalida')
        firstScore = float(input())

    secondScore = float(input())

    while secondScore < 0 or secondScore > 10:
        print('nota invalida')
        secondScore = float(input())

    print(f'media = {((secondScore + firstScore)/2):.2f}')

scoreValidation()
