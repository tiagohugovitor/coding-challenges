# 1150-exceedingZ.py
# Problem: Exceeding Z
# Link: https://judge.beecrowd.com/en/problems/view/1150
# Solved on: 2024-08-22

def exceedingZ():
    x = int(input())
    z = x
    while z <= x:
        z = int(input())

    sum = x
    numbers = 1
    while sum <= z:
        x += 1
        sum += x
        numbers += 1
        
    print(f'{numbers}')

exceedingZ()