# 1985-macPronalts.py
# Problem: macPRONALTS
# Link: https://judge.beecrowd.com/en/problems/view/1985
# Solved on: 2024-08-28

def macPronalts():
    price = {
        1001: 1.5,
        1002: 2.5,
        1003: 3.5,
        1004: 4.5,
        1005: 5.5,
    }
    total = 0
    sells = int(input())
    for _ in range(sells):
        id, amount = map(int, input().split())
        total += amount * price[id]
    
    print(f'{total:.2f}')

macPronalts()
