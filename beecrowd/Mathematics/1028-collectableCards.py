# 1028-collectableCards.py
# Problem: Collectable Cards
# Link: https://judge.beecrowd.com/en/problems/view/1028
# Solved on: 2024-11-18

import sys

def collectableCards():
    input_data = sys.stdin.read().splitlines()
    i = 1

    for _ in range(int(input_data[0])):
        a, b = map(int, input_data[i].split())
        i += 1

        if b > a:
            b, a = a, b
        
        while b != 0:
            a, b = b, a % b

        mdc = a                                                                                                                                                                  

        print(mdc)

collectableCards()
