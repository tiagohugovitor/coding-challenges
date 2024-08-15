# 0414-thirdMaximumNumber.py
# Problem: Third Maximum Number
# Link: https://leetcode.com/problems/third-maximum-number/description/
# Solved on: 2024-08-15

# Time complexity: O(n)
# Space complexity: O(1)
# Description: This function returns the third distinct maximum number in a list of integers `nums`. It maintains an array 
# `maxs` of three elements to track the top three maximum values, initialized to negative infinity (`-inf`). As it iterates 
# through the list, it updates `maxs` based on the current number’s comparison with the elements of `maxs`. If the third 
# maximum exists, it returns that value; otherwise, it returns the largest value in the list.

def thirdMax(nums):
    maxs = [float('-inf')] * 3

    for num in nums:
        if num > maxs[0]:
            maxs[2] = maxs[1]
            maxs[1] = maxs[0]
            maxs[0] = num
        elif num > maxs[1] and num != maxs[0]:
            maxs[2] = maxs[1]
            maxs[1] = num
        elif num > maxs[2] and num != maxs[1] and num != maxs[0]:
            maxs[2] = num

    if maxs[2] != float('-inf'):
        thirdMax = maxs[2]
    else:
        thirdMax = maxs[0]

    return thirdMax

print(thirdMax([1,2,2,5,3,5]))