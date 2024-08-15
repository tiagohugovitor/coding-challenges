# 0414-findDisappearedNumbers.py
# Problem: Find All Numbers Disappeared in an Array
# Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
# Solved on: 2024-08-15

# Time complexity: O(n)
# Space complexity: O(1)
# Description: This function uses a cyclic sort approach to place each number at its correct index.
# If a number is already in its correct position or is a duplicate, the loop continues. After rearranging,
# a second loop identifies the indices where the number is not in the correct position, indicating the 
# missing numbers.

def findDisappearedNumbers(nums):
    n = len(nums)
    i = 0
    result = []
    while i < n:
        if nums[i] == i + 1 or nums[i] == nums[nums[i] - 1]:
            i += 1
        else:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    for i in range(n):
        if nums[i] != i + 1:
            result.append(i + 1)

    return result

print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))