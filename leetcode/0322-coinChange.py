# 0322-coinChange.py
# Problem: Coin Change
# Link: https://leetcode.com/problems/coin-change/description/
# Solved on: 2024-07-13

# Time complexity: O(n * m), where n is the number of coins and m is the amount.
# Space complexity: O(m)
# Description: This function uses dynamic programming to calculate the minimum number of coins
# needed to make a change of amount 'm' given an array 'coins'. We use an auxiliary array
# 'numberOfCoins' to store the minimum number of coins required to make change for each value 
# from 0 to 'm'.

def coinChange(coins, amount):
    numberOfCoins = [float('inf')] * (amount + 1)
    numberOfCoins[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            numberOfCoins[i] = min(numberOfCoins[i], numberOfCoins[i-coin] + 1)
    
    return -1 if numberOfCoins[amount] == float('inf') else numberOfCoins[amount]
    

print(coinChange([1,3,4,], 6))