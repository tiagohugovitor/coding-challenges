# 1142-PUM.py
# Problem: PUM
# Link: https://judge.beecrowd.com/en/problems/view/1142
# Solved on: 2024-08-21

def pum():
    n = int(input())
    numbers = n * 4

    for number in range(1, numbers + 1):
        if number % 4 == 0:
            print('PUM')
        else:
            print(f'{number} ', end='') 

pum()
