# 0045-jumpGame2.py
# Problem: Jump Game II
# Link: https://leetcode.com/problems/jump-game-ii/description/
# Solved on: 2024-08-16

# Time complexity: O(n)
# Space complexity: O(1)
# Description: This function computes the minimum number of jumps required to reach the last index of the `nums` array. 
# Starting from the first index, it iteratively determines the farthest position that can be reached in each jump 
# by checking the possible ranges from the current position (`stand`). It then updates the current position to the best 
# possible next position (`nextJump`) and increments the jump count. The process continues until the last index 
# (`goal`) is within reach.

def jump(nums):
    goal = len(nums) - 1
    if goal == 0:
        return 0
    jumps = 1
    stand = 0
    nextJump = 0
    while stand + nums[stand] < goal:
        nextJump = stand + 1
        for i in range(1, nums[stand]):
            if nums[stand + i + 1] > nums[nextJump] - (stand + i + 1 - nextJump):
                nextJump = stand + i + 1
        stand = nextJump
        jumps += 1
    return jumps

print(jump([2,3,1,1,4]))