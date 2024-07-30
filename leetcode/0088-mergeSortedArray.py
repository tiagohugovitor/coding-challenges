# 0088-mergeSortedArray.py
# Problem: Merge Sorted Array
# Link: https://leetcode.com/problems/merge-sorted-array/description/
# Solved on: 2024-07-29

# Time complexity: O(m + n)
# Space complexity: O(m + n)
# Description: This function merges two sorted arrays, `nums1` and `nums2`, into a single sorted array.
# It uses auxiliary arrays to store elements from `nums1` and `nums2`, then merges them back into `nums1`.

def merge(nums1, m, nums2, n):
    auxiliary1 = [0] * m
    auxiliary2 = [0] * n

    for i in range(m):
        auxiliary1[i] = nums1[i]

    for i in range(n):
        auxiliary2[i] = nums2[i]
    
    pointer1 = 0
    pointer2 = 0

    while pointer1 < m and pointer2 < n:
        if auxiliary1[pointer1] <= auxiliary2[pointer2]:
            nums1[pointer1 + pointer2] = auxiliary1[pointer1]
            pointer1 += 1
        else:
            nums1[pointer1 + pointer2] = auxiliary2[pointer2]
            pointer2 += 1

    while pointer1 < m:
        nums1[pointer1 + pointer2] = auxiliary1[pointer1]
        pointer1 += 1
    
    while pointer2 < n:
        nums1[pointer1 + pointer2] = auxiliary2[pointer2]
        pointer2 += 1

# Time complexity: O(m + n)
# Space complexity: O(1)
# Description: This in-place function merges two sorted arrays, `nums1` and `nums2`, into a single sorted array.
# It starts from the end of both arrays and places the largest elements at the end of `nums1`.

def mergeInPlace(nums1, m, nums2, n):
    pointer1 = m -1
    pointer2 = n - 1

    while pointer1 >= 0 and pointer2 >= 0:
        if nums1[pointer1] > nums2[pointer2]:
            nums1[pointer1 + pointer2 + 1] = nums1[pointer1]
            pointer1 -= 1
        else:
            nums1[pointer1 + pointer2 + 1] = nums2[pointer2]
            pointer2 -= 1

    while pointer1 >= 0:
        nums1[pointer1] = nums1[pointer1]
        pointer1 -= 1
    
    while pointer2 >= 0:
        nums1[pointer2] = nums2[pointer2]
        pointer2 -= 1
    
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
mergeInPlace(nums1, 3, nums2, 3)
print(nums1)