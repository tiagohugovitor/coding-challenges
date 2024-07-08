# 015-3sum.py
# Problem: 3Sum
# Link: https://leetcode.com/problems/3sum/description/
# Solved on: 2024-06-28


# Time complexity: O(n³)
# Description: This function employs a brute-force approach to solve the 3 sum.
# It iterates through all possible triples of elements in the list to find all that sums 0.

def threeSumCubic(nums):
    solutions = []
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if(nums[i] + nums[j] + nums[k] == 0):
                    if([nums[i], nums[j], nums[k]] not in solutions
                       and [nums[i], nums[k], nums[j]] not in solutions
                       and [nums[j], nums[i], nums[k]]  not in solutions
                       and [nums[j], nums[k], nums[i]]  not in solutions
                       and [nums[k], nums[j], nums[i]]  not in solutions
                       and [nums[k], nums[i], nums[j]]  not in solutions
                    ):
                        solutions.append([nums[i], nums[j], nums[k]])
    return solutions


def threeSumCubicSet(nums):
    solutions = set()
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if(nums[i] + nums[j] + nums[k] == 0):
                    solutions.add(tuple(sorted((nums[i], nums[j], nums[k]))))
    return [list(triplet) for triplet in solutions]


def threeSumSort(nums):
    solutions = []
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        p = i + 1
        q = len(nums) - 1
        while p < q:
            sum = nums[i] + nums[p] + nums[q]
            if sum > 0:
                q -= 1
            elif sum < 0:
                p += 1
            else:
                solutions.append([nums[i], nums[p], nums[q]])
                while p < q and nums[p] == nums[p + 1]:
                    p += 1
                while p < q and nums[q] == nums[q - 1]:
                    q -= 1
                p += 1
                q -= 1
    return solutions


print(threeSumSort([-1,0,1,2,-1,-4]))