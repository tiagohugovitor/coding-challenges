# 0035-searchInsert.py
# Problem: Search Insert Position
# Link: https://leetcode.com/problems/search-insert-position/description/
# Solved on: 2024-07-14

# Time complexity: O(log n).
# Description: The function implements a binary search to found the place of
# target inside the array.

def searchInsert(nums, target):
    def binarySearch(nums, start, end, target):
        if start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                return binarySearch(nums, start, mid - 1, target)
            if nums[mid] < target:
                return binarySearch(nums, mid + 1, end, target)
        else:
            if nums[start] == target or nums[start] > target:
                return start
            if nums[start] < target:
                return start + 1
    
    return binarySearch(nums, 0, len(nums) - 1, target)

print(searchInsert([1,3,5,6], 7))