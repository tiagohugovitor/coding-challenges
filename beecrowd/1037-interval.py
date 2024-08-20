# 1037-interval.py
# Problem: Interval
# Link: https://judge.beecrowd.com/en/problems/view/1037
# Solved on: 2024-08-18

def interval():

    number = float(input())
    if number < 0 or number > 100:
        print('Fora de intervalo')
        return
    if number <= 25:
        print('Intervalo [0,25]')
        return
    if number <= 50:
        print('Intervalo (25,50]')
        return
    if number <= 75:
        print('Intervalo (50,75]')
        return
    if number <= 100:
        print('Intervalo (75,100]')
    return

interval()