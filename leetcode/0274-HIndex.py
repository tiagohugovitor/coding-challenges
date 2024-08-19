# 0274-hIndex.py
# Problem: H-Index
# Link: https://leetcode.com/problems/h-index/description
# Solved on: 2024-08-16

# Time complexity: O(log n).
# Description: The function implements a binary search to found the place of
# target inside the array.

import random

def particionate(array, start, end):
    pivot = random.randint(start, end)
    array[pivot], array[start] = array[start], array[pivot]
    right = start + 1
    left = start + 1
    while right <= end:
        if array[right] > array[start]:
            array[right], array[left] = array[left], array[right]
            left += 1
        right += 1
    array[start], array[left - 1] = array[left - 1], array[start]
    return left - 1

def quickSort(array, start, end):
    if start < end:
        pivot = particionate(array, start, end)
        quickSort(array, start, pivot - 1)
        quickSort(array, pivot + 1, end)

def hIndex(citations):
    start = 0
    end = len(citations) - 1
    
    quickSort(citations, start, end)

    count = 0

    while count < len(citations) and citations[count] >= count+1:
            count += 1
    return count

print(hIndex([100, 50]))