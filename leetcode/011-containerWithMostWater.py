# 011-containerWithMostWater.py
# Problem: Container With Most Water
# Link: https://leetcode.com/problems/container-with-most-water/description/
# Solved on: 2024-06-28


# Time complexity: O(n²)
# Description: This function employs a brute-force approach to solve the Container With Most Water problem.
# It iterates through all possible pairs of elements in the list to find the maximum container

def maxAreaQuadratic(height):
    max = 0
    for i in range(len(height) - 1):
        for j in range(i, len(height)):
            currentArea = min(height[i], height[j]) * (j-i)
            if(currentArea > max):
                max = currentArea
    return max


# Time complexity: O(n)
# Description: This function uses two pointers (p and q) to find two numbers that has the max
# container. It adjusts the pointers based on whether is the smaller height.

def maxArea(height):
    max = 0
    p = 0
    q = len(height) - 1
    while p < q:
        currentArea = min(height[p], height[q]) * (q-p)
        if(currentArea > max):
            max = currentArea
        if height[p] < height[q]:
            p += 1
        else:
            q -= 1
    return max

print(maxArea([1,8,6,2,5,4,8,3,7]))