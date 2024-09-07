# 2709-coinsOfRobbie.py
# Problem: The Coins of Robbie
# Link: https://judge.beecrowd.com/en/problems/view/2709
# Solved on: 2024-09-06

import math

def coinsOfRobbie():
    while True:
        try:
            amountOfCoins = int(input())
            coins = [0] * amountOfCoins
            for coin in range(amountOfCoins):
                coins[coin] = int(input())
            n = int(input())

            totalSum = 0
            index = amountOfCoins - 1

            while index >= 0:
                totalSum += coins[index]
                index -= n
            
            if totalSum < 2:
                isPrime = False
            
            else:
                isPrime = True
                for i in range(2, int(math.sqrt(totalSum)) + 1):
                    if totalSum % i == 0:
                        isPrime = False
                        break

            if isPrime:
                print('You’re a coastal aircraft, Robbie, a large silver aircraft.')
            else:
                print('Bad boy! I’ll hit you.')

        except EOFError:
            break

coinsOfRobbie()
