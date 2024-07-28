# 0027-removeDuplicates.py
# Problem: Remove Element
# Link: https://leetcode.com/problems/remove-element/description/
# Solved on: 2024-07-21

# Time complexity: O(n)
# Space complexity: O(1)
# Description: This function removes all instances of the target element from the list `nums` and returns the new length 
# of the list. It uses two pointers, `left` and `right`, to traverse the list from both ends. If the element at `left` 
# equals the target, it swaps it with the element at `right` and decrements `right`. Otherwise, it increments `left`. 
# The process continues until `right` is less than `left`.

def removeElement(nums, target):
    left = 0
    right = len(nums) - 1

    if len(nums) == 1:
        return 1 if nums[0] != target else 0

    while right >= left:
        if nums[left] == target:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
        else:
            left += 1

    return left

print(removeElement([0,0,1,1,1,2,2,3,3,4], 2))
