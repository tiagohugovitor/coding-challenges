# 2708-tourists.py
# Problem: Tourists in the Huacachina Park
# Link: https://judge.beecrowd.com/en/problems/view/2708
# Solved on: 2024-09-06

def tourists():
    cars = 0
    people = 0
    while True:
        data = input()
        if data == 'ABEND':
            break
        action, amount = data.split()
        if action == 'SALIDA':
            people += int(amount)
            cars += 1
        if action == 'VUELTA':
            people -= int(amount)
            cars -= 1
    
    print(people)
    print(cars)

tourists()
