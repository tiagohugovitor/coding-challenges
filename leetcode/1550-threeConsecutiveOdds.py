# 1550-threeConsecutiveOdds.py
# Problem: Three Consecutive Odds
# Link: https://leetcode.com/problems/three-consecutive-odds/description/
# Solved on: 2024-07-07

# Time complexity: O(n)
# Description: This function iterates through all the array once and count the
# odds numbers in sequence.

def threeConsecutiveOdds(arr):
    amount = 0
    for i in range(len(arr)):
        if arr[i]%2 != 0:
            amount += 1
        else:
            amount = 0
        if amount == 3:
            return True
    return False

print(threeConsecutiveOdds([2,6,4,1]))