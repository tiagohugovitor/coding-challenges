# 0026-removeDuplicates.py
# Problem: Remove Duplicates from Sorted Array
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# Solved on: 2024-07-21

# Time complexity: O(n)
# Space complexity: O(1)
# Description: This function identifies the length of the longest subsequence of unique elements in a sorted list `nums`.
# If `nums` has only one element, it returns 1. Otherwise, it iterates through `nums`, updating the `left` pointer 
# whenever a larger unique element is found. The `right` pointer traverses the list, ensuring all elements are considered.
# Finally, it returns the count of unique elements.

def removeDuplicates(nums):
    left = 0
    right = 1

    if len(nums) == 1:
        return 1

    while right < len(nums):
        if nums[right] > nums[left]:
            left += 1
            nums[left] = nums[right]
        right += 1
        
    return left + 1

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
