# 3039-santasToys.py
# Problem: Santa's Toys
# Link: https://judge.beecrowd.com/en/problems/view/3039
# Solved on: 2024-10-21

def santasToys():
    kids = int(input())
    males = 0
    females = 0

    for _ in range(kids):
        name, sex = input().split()
        if sex == 'F':
            females += 1
        else:
            males += 1

    print(f'{males} carrinhos')
    print(f'{females} bonecas')

santasToys()
