# 2721-indecisionOfReindeers.py
# Problem: Indecision of Reindeers
# Link: https://judge.beecrowd.com/en/problems/view/2721
# Solved on: 2024-09-06

def indecisionOfReindeers():
    order = ['Rudolph', 'Dasher', 'Dancer', 'Prancer', 'Vixen', 'Comet', 'Cupid', 'Donner', 'Blitzen']
    snowballs = list(map(int, input().split()))
    totalSum = sum(snowballs)
    totalSum = totalSum % 9
    print(order[totalSum])

indecisionOfReindeers()
