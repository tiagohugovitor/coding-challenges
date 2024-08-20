# 1017-fuelSpent.py
# Problem: Fuel Spent
# Link: https://judge.beecrowd.com/en/problems/view/1017
# Solved on: 2024-08-18

def fuelSpent():
    time = int(input())
    speed = int(input())
    fuel = (speed * time) / 12
    print(f'{fuel:.3f}')

fuelSpent()