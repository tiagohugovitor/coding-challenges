# 0033-searchInRotatedSortedArray.py
# Problem: Search in Rotated Sorted Array
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
# Solved on: 2024-08-01

# Time complexity: O(log n)
# Space complexity: O(log n)
# Description: This function searches for a target value in a rotated sorted array `nums`. It uses a modified binary
# search approach to handle the rotation. The `binarySearch` function is called recursively to find the target value
# by adjusting the search range based on the midpoint and the sorted portions of the array. If the target is found, 
# the index is returned; otherwise, -1 is returned.

def searchRecursive(nums, target):
    def binarySearch(nums, start, end, target):
        if start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[end] and target > nums[mid] and target <= nums[end]:
                return binarySearch(nums, mid + 1, end, target)
            if nums[mid] > nums[end] and (target > nums[mid] or target <= nums[end]):
                return binarySearch(nums, mid + 1, end, target)    
            if nums[mid] > nums[start] and target < nums[mid] and target >= nums[start]:
                return binarySearch(nums, start, mid - 1, target)
            if nums[mid] < nums[start] and (target >= nums[start] or target < nums[mid]):
                return binarySearch(nums, start, mid - 1, target)
    
    index = binarySearch(nums, 0, len(nums) - 1, target)
    return index if index != None else -1

# Time complexity: O(log n)
# Space complexity: O(1)
# Description: This function searches for a target value in a rotated sorted array `nums` using an iterative approach.
# It performs a binary search, adjusting the search range based on the midpoint and the sorted portions of the array.
# If the target is found, the index is returned; otherwise, -1 is returned.

def searchIterative(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < nums[end] and target > nums[mid] and target <= nums[end]:
            start = mid + 1
        elif nums[mid] > nums[end] and (target > nums[mid] or target <= nums[end]):
            start = mid + 1
        elif nums[mid] > nums[start] and target < nums[mid] and target >= nums[start]:
            end = mid - 1
        elif nums[mid] < nums[start] and (target >= nums[start] or target < nums[mid]):
            end = mid - 1
        else:
            return -1
    
    return -1

print(searchIterative([4,5,6,7,0,1,2], 2))