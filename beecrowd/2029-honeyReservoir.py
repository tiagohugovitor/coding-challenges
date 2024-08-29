# 2029-honeyReservoir.py
# Problem: Honey Reservoir
# Link: https://judge.beecrowd.com/en/problems/view/2029
# Solved on: 2024-08-28

def honeyReservoir():
    while True:
        try:
            volume = float(input())
            diameter = float(input())
            area = 3.14 * pow(diameter/2, 2)
            height = volume / area 
            print(f'ALTURA = {height:.2f}')
            print(f'AREA = {area:.2f}')
        except EOFError:
            break

honeyReservoir()
