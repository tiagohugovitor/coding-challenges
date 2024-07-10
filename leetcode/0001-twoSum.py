# 0001-twoSum.py
# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/description/
# Solved on: 2024-06-27


# Time complexity: O(n²)
# Description: This function employs a brute-force approach to solve the Two Sum problem.
# It iterates through all possible pairs of elements in the list to find two numbers that
# sum up to the target.

def twoSumQuadratic(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# Time complexity: O(nlogn)
# Description: This function first sorts the input array and then uses two pointers (p and q)
# to find two numbers that sum up to the target. It adjusts the pointers based on whether the
# current sum is greater than or less than the target, ensuring an efficient search.


def twoSumSort(nums, target):
    arr = sorted(nums)

    p = 0
    q = len(nums) - 1

    while p<q:
        if arr[p] + arr[q] == target:
            break
        if arr[p] + arr[q] > target:
            q -= 1
        if arr[p] + arr[q] < target:
            p += 1

    firstIndex = -1
    lastIndex = -1

    for i in range(len(nums)):
        if nums[i] == arr[p] and firstIndex == -1:
            firstIndex = i
        elif nums[i] == arr[q]:
            lastIndex = i

    return [firstIndex, lastIndex]

# Time complexity: O(n)
# Space complexity: O(n)
# Optimal solution.
# Description: This function efficiently solves the Two Sum problem using a dictionary
# (complementary) to track the complement of each number needed to reach the target.
# It iterates through the array once, checking if the current number's complement exists
# in the dictionary.

def twoSum(nums, target):
    complementary = {}

    for i in range(len(nums)):
        if nums[i] in complementary:
            return [complementary[nums[i]], i]
        else:
            complementary[target - nums[i]] = i
    

print(twoSumQuadratic([3,2,4], 6))
print(twoSumSort([3,2,4], 6))
print(twoSum([3,2,4], 6))