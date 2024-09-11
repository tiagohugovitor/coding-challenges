# 2712-vehicularRestriction.py
# Problem: Vehicular Restriction
# Link: https://judge.beecrowd.com/en/problems/view/2712
# Solved on: 2024-09-06

import re

def vehicularRestriction():
    restriction = {
        '1': 'MONDAY',
        '2': 'MONDAY',
        '3': 'TUESDAY',
        '4': 'TUESDAY',
        '5': 'WEDNESDAY',
        '6': 'WEDNESDAY',
        '7': 'THURSDAY',
        '8': 'THURSDAY',
        '9': 'FRIDAY',
        '0': 'FRIDAY'
    }
    tests = int(input())
    for _ in range(tests):
        card = input()

        valid = re.fullmatch(r'[A-Z]{3}-[0-9]{4}', card)

        if not valid:
            print('FAILURE')
        else:
            print(restriction[card[7]])


vehicularRestriction()
