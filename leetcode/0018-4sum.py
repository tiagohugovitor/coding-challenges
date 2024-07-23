# 0018-4Sum.py
# Problem: 4Sum
# Link: https://leetcode.com/problems/4sum/description/
# Solved on: 2024-07-22

# Time complexity: O(n^3)
# Space complexity: O(1)
# Description: This function finds all unique quadruplets in the array that sum up to the given target.
# It first sorts the array to facilitate the two-pointer approach. It then iterates through
# the array, using two nested loops to fix the first two numbers, and a two-pointer technique
# to find the other two numbers that complete the quadruplet. Duplicate quadruplets are avoided
# by skipping over duplicate numbers during the iteration.

def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    res = []

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue 

        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left = j + 1
            right = n - 1

            while left < right:
                currentSum = nums[i] + nums[j] + nums[left] + nums[right]
                if currentSum == target:
                    res.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1 
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1 
                    left += 1
                    right -= 1
                elif currentSum < target:
                    left += 1
                else:
                    right -= 1

    return res

print(fourSum([1,0,-1,0,-2,2], 0))