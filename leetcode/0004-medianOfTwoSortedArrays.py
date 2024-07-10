# 0004-medianOfTwoSortedArrays.py
# Problem: Median of Two Sorted Arrays
# Link: https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# Solved on: 2024-06-27

# Time complexity: O(m + n)
# Description: This function merges nums1 and nums2 into a sorted merged
# array and calculates the median. It runs through nums1 and nums2 once each.

def findMedianSortedArrays(nums1, nums2):
    size = len(nums1) + len(nums2)
    merged = [0] * size
    index = 0
    p = 0
    q = 0
    
    while p < len(nums1) and q < len(nums2):
        if nums1[p] < nums2[q]:
            merged[index] = nums1[p]
            p += 1
        else:
            merged[index] = nums2[q]
            q += 1
        index += 1
    
    while p < len(nums1):
        merged[index] = nums1[p]
        p += 1
        index += 1

    while q < len(nums2):
        merged[index] = nums2[q]
        q += 1
        index += 1

    if len(merged)%2 == 0:
        median = (merged[len(merged) // 2 - 1] + merged[len(merged) // 2 ]) / 2
    else:
        median = merged[len(merged) // 2]

    return median

print(findMedianSortedArrays([1,2], [3,4]))