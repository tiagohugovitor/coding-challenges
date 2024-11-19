# 1555-functions.py
# Problem: Functions
# Link: https://judge.beecrowd.com/en/problems/view/1555
# Solved on: 2024-11-18

import sys

def collectableCards():
    input_data = sys.stdin.read().splitlines()
    i = 1

    for _ in range(int(input_data[0])):
        x, y = map(int, input_data[i].split())
        i += 1
        
        rafael = 9 * x * x + y * y
        beto = 2 * x * x + 5 * 5 * y * y
        carlos =  y*y*y - 100 * x 
        
        if rafael > beto:
            winner = 'Rafael' if rafael > carlos else 'Carlos'
        else:
            winner = 'Beto' if beto > carlos else 'Carlos'

        print(f'{winner} ganhou')
        
collectableCards()
