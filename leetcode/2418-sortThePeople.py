# 2418-sortThePeople.py
# Problem: Sort the People
# Link: https://leetcode.com/problems/sort-the-people/description/
# Solved on: 2024-07-22

# Time complexity: O(n log n)
# Space complexity: O(log n) on average due to the recursion stack
# Description: This function sorts people based on their heights in descending order using the quicksort algorithm.
# The `particionate` function partitions the list around a randomly chosen pivot, ensuring all elements greater than the pivot
# are on the left and all elements smaller are on the right.
# The `quickSortPeople` function uses a tail-recursive approach for sorting. Instead of making a recursive call for both halves
# of the partitioned list, it sorts the left half recursively and iterates on the right half, converting the right half's
# recursive call into an iteration to optimize the recursion depth and prevent stack overflow.

import random

def sortPeople(names, heights):

    def particionate(names, heights, start, end):
        pivot = random.randint(start,end)
        heights[start], heights[pivot] = heights[pivot], heights[start]
        names[start], names[pivot] = names[pivot], names[start]
        left = start + 1
        right = start + 1
        while right <= end:
            if heights[right] > heights[start]:
                heights[left], heights[right] = heights[right], heights[left]
                names[left], names[right] = names[right], names[left]
                left += 1
            right += 1
        heights[start], heights[left-1] = heights[left-1], heights[start]
        names[start], names[left-1] = names[left-1], names[start]
        return left - 1

    def quickSortPeople(names, heights, start, end):
        while start < end:
            pivot = particionate(names, heights, start, end)
            quickSortPeople(names, heights, start, pivot -1)
            start = pivot + 1
     
    quickSortPeople(names, heights, 0, len(heights) - 1)

    return names

print(sortPeople(["Mary","John","Emma"],[180,165,170]))
