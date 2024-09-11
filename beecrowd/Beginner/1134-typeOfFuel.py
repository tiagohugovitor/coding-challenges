# 1134-typeOfFuel.py
# Problem: Type of Fuel
# Link: https://judge.beecrowd.com/en/problems/view/1134
# Solved on: 2024-08-21

def typeOfFuel():
    customers = [0] * 3
    fuel = 0

    while True:
        fuel = int(input())

        if fuel == 4:
            break
        
        if fuel in [1, 2, 3]:
            customers[fuel - 1] += 1
        
    print(f'MUITO OBRIGADO')
    print(f'Alcool: {customers[0]}')
    print(f'Gasolina: {customers[1]}')
    print(f'Diesel: {customers[2]}')

typeOfFuel()
