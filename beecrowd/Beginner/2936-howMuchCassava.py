# 2936-howMuchCassava.py
# Problem: How Much Cassava?
# Link: https://judge.beecrowd.com/en/problems/view/2936
# Solved on: 2024-10-15

def howMuchCassava():
    cassavaAmount = 225
    portionSizes = [300, 1500, 600, 1000, 150]

    for portion in portionSizes:
        order = int(input())
        cassavaAmount += portion * order
    
    print(cassavaAmount)

howMuchCassava()
