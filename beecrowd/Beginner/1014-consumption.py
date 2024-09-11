# 1014-consumption.py
# Problem: Consumption
# Link: https://judge.beecrowd.com/en/problems/view/1014
# Solved on: 2024-08-18

def consumption():
    distance = int(input())
    fuel = float(input())
    average = distance / fuel
    print(f'{average:.3f} km/l')

consumption()