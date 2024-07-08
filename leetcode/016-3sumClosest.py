# 016-3sumClosest.py
# Problem: 3Sum Closest
# Link: https://leetcode.com/problems/3sum-closest/description/
# Solved on: 2024-06-28

import math

# Time complexity: O(n³)
# Description: This function employs a brute-force approach to solve the 3 sum closest.
# It iterates through all possible triples of elements in the list to find the closest to the target.

def threeSumClosestCubic(nums, target):
    closest = math.inf
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                sum = nums[i] + nums[j] + nums[k]
                if (abs(closest) > abs(sum - target)):
                    closest = sum
    return closest


# Time complexity: O(n²)
# Description: This function employs a two pointer approach to solve the 3 sum closest.
# It fixs one number and then iterates throug the array with two pointer in the list to
# find the closest sum to the target.

def threeSumClosest(nums, target):
    nums.sort()
    closest = math.inf
    for i in range(0, len(nums) - 2):
        p = i + 1
        q = len(nums) - 1
        while p < q:
            if(abs(nums[p] + nums[q] + nums[i] - target) < abs(closest - target)):
                closest = nums[p] + nums[q] + nums[i]
            if(nums[p] + nums[q] + nums[i] > target):
                q -= 1
            else:
                p += 1    
    return closest

print(threeSumClosest([0,0,0], 1))