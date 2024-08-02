# 0034-searchRange.py
# Problem: Find First and Last Position of Element in Sorted Array
# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
# Solved on: 2024-08-01

# Time complexity: O(n)
# Space complexity: O(1)
# Description: This function finds the first and last positions of a given target in a sorted array.
# It uses binary search to locate one occurrence of the target and then expands to the left and right
# to find the first and last positions. The overall time complexity is O(n) due to the potential linear
# search from the middle to the ends of the target sequence, and space complexity is O(1).

def searchRange(nums, target):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            p = mid
            q = mid
            while (p > -1 and nums[p] == target) or (q < len(nums) and nums[q] == target):
                if p > -1 and nums[p] == target:
                    p -= 1
                if q < len(nums) and nums[q] == target:
                    q += 1
            return [p + 1, q - 1]
        if nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return [-1, -1]

# Time complexity: O(log n)
# Space complexity: O(1)
# Description: This function finds the first and last positions of a given target in a sorted array.
# It uses two separate binary searches to locate the end index and the start index of the target.
# The first binary search finds the end index by ensuring that the mid element is the last occurrence
# of the target. The second binary search finds the start index by ensuring that the mid element is
# the first occurrence of the target. The overall time complexity is O(log n) and space complexity is O(1).

def searchRangeOptimized(nums, target):
    startIndex = -1
    endIndex = -1
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target and (mid + 1 == len(nums) or nums[mid+1] != target):
            endIndex = mid
        if nums[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1

    start = 0
    end = len(nums) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target and (mid == 0 or nums[mid-1] != target):
            startIndex = mid
        if nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return [startIndex, endIndex]

print(searchRangeOptimized([2,2], 2))