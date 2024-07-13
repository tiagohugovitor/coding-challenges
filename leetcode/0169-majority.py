# 0169-majority.py
# Problem: Majority
# Link: https://leetcode.com/problems/majority-element/
# Solved on: 2024-07-13

# Time complexity: O(n)
# Description: This function uses Boyer-Moore voting algorithm to iterate only once
# over the array to find the majority element

def majority(nums):
    candidate = None
    votes = 0

    for num in nums:
        if votes == 0:
            candidate = num
            votes = 1
        elif candidate == num:
            votes += 1
        else:
            votes -= 1
    return candidate

print(majority([1, 2, 1, 1, 3, 1, 1, 2, 1]))