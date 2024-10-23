# 3147-battleOfFiveArmies.py
# Problem: The Battle of the Five Armies
# Link: https://judge.beecrowd.com/en/problems/view/3147
# Solved on: 2024-10-23

def battleOfFiveArmies():
    humans, elves, dwarves, orcs, wargs, eagles = map(int, input().split())

    goodSide = humans + elves + dwarves + eagles
    badSide = orcs + wargs

    if goodSide >= badSide:
        print('Middle-earth is safe.')
    else:
        print('Sauron has returned.')

battleOfFiveArmies()
