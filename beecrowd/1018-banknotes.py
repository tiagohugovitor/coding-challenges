# 1018-banknotes.py
# Problem: Banknotes
# Link: https://judge.beecrowd.com/en/problems/view/1018
# Solved on: 2024-08-18

def banknotes():
    change = int(input())
    notes = [100, 50, 20, 10, 5, 2, 1]
    print(f'{change}')
    for note in notes:
        amount = change // note
        change = change % note
        print(f'{amount} nota(s) de R$ {note},00')

banknotes()