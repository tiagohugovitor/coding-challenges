# 0031-nextPermutation.py
# Problem: Next Permutation
# Link: https://leetcode.com/problems/next-permutation/description/
# Solved on: 2024-07-28

# Time complexity: O(n^2)
# Space complexity: O(1)
# Description: This function modifies the list `nums` to the next lexicographical permutation. 
# It finds the rightmost ascent to determine `swapIndex`. If no ascent is found, the list is reversed.
# Otherwise, it swaps the appropriate elements and sorts the subarray from `swapIndex` using insertion sort.

def nextPermutation(nums):
    if len(nums) == 1:
        return

    def insertionSort(arr, start, end):
        for i in range(start+1, end + 1):
            temp = arr[i]
            j = i
            while temp < arr[j-1] and j > start:
                arr[j] = arr[j-1]
                j -= 1
            arr[j] = temp

    swapIndex = -1
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] > nums[i-1]:
            swapIndex = i
            break

    if swapIndex == -1:
        left = 0
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return

    index = swapIndex
    for i in range(swapIndex, len(nums)):
        if nums[i] > nums[swapIndex-1] and nums[i]<nums[index]:
            index = i
    nums[swapIndex - 1], nums[index] = nums[index], nums[swapIndex - 1]

    insertionSort(nums, swapIndex, len(nums) - 1)

nums = [1,3,2]
nextPermutation(nums)
print(nums)
