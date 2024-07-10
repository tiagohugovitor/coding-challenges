# 0350-intersect.py
# Problem: Intersection of Two Arrays II
# Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/description/?
# Solved on: 2024-07-07

# Time complexity: O(m log m + n log n)
# Space complexity: O(min(m, n))
# Description: This function sorts both arrays and uses two pointers to find common elements. 
# It iterates through both arrays simultaneously, adding matching elements to the result list.

def intersect(nums1, nums2):
    nums1.sort()
    nums2.sort()
    p = 0
    q = 0
    result = []
    while p < len(nums1) and q < len(nums2):
        if(nums1[p] == nums2[q]):
            result.append(nums1[p])
            p += 1
            q += 1
        elif nums1[p] < nums2[q]:
            p += 1
        else:
            q += 1
    return result

print(intersect([4,9,5], [9,4,9,8,4]))