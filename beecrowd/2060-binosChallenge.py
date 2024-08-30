# 2060-binosChallenge.py
# Problem: Bino's Challenge
# Link: https://judge.beecrowd.com/en/problems/view/2060
# Solved on: 2024-08-29

def binosChallenge():
    multiplesOf2 = 0
    multiplesOf3 = 0
    multiplesOf4 = 0
    multiplesOf5 = 0
    amount = int(input())
    numbers = list(map(int, input().split()))

    for number in numbers:
        if number % 2 == 0:
            multiplesOf2 += 1
        if number % 3 == 0:
            multiplesOf3 += 1
        if number % 4 == 0:
            multiplesOf4 += 1
        if number % 5 == 0:
            multiplesOf5 += 1

    print(f'{multiplesOf2} Multiplo(s) de 2')
    print(f'{multiplesOf3} Multiplo(s) de 3')
    print(f'{multiplesOf4} Multiplo(s) de 4')
    print(f'{multiplesOf5} Multiplo(s) de 5')
binosChallenge()
