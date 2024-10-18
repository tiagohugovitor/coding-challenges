# 2808-knightsAgain.py
# Problem: Knights Again
# Link: https://judge.beecrowd.com/en/problems/view/2808
# Solved on: 2024-10-17

def knightsAgain():
    letterToNumber = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
    }

    position, target = input().split()
    
    if (abs(letterToNumber[position[0]] - letterToNumber[target[0]]) == 1 and abs(int(position[1]) - int(target[1])) == 2) or (abs(letterToNumber[position[0]] - letterToNumber[target[0]]) == 2 and abs(int(position[1]) - int(target[1])) == 1):
        print('VALIDO')
    else:
        print('INVALIDO')

knightsAgain()
