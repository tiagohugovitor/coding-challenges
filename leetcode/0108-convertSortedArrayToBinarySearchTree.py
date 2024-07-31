# 0108-convertSortedArrayToBinarySearchTree.py
# Convert Sorted Array to Binary Search Tree
# Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
# Solved on: 2024-07-30

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time complexity: O(n)
# Space complexity: O(log n) due to the recursion stack
# Description: This function converts a sorted array into a height-balanced binary search tree (BST) using a recursive approach.
# It recursively selects the middle element of the current subarray as the root and constructs left and right subtrees from the 
# left and right subarrays respectively. The function returns the root of the BST.

def sortedArrayToBSTRecursive(nums):
    if not nums:
        return []

    def convertToBst(nums, start, end):
        if start == end:
            return TreeNode(nums[start])   
        if start < end:
            mid = (start + end) // 2
            current = TreeNode(nums[mid])
            current.left = convertToBst(nums, start, mid-1)
            current.right = convertToBst(nums, mid + 1, end)
            return current
        return None

    return convertToBst(nums, 0, len(nums) - 1)

# Time complexity: O(n)
# Space complexity: O(n)
# Description: This function converts a sorted array into a height-balanced binary search tree (BST) using an iterative approach.
# It uses a stack to simulate the recursive approach, maintaining the indices of the subarrays to construct the left and right subtrees.
# The function returns the root of the BST.

def sortedArrayToBSTIterative(nums):
    if not nums:
        return None

    root = TreeNode(0)
    stack = [(root, 0, len(nums) - 1)]

    while stack:
        node, start, end = stack.pop()
        mid = (start + end) // 2
        node.val = nums[mid]

        if start <= mid - 1:
            node.left = TreeNode(0)
            stack.append((node.left, start, mid - 1))
        if mid + 1 <= end:
            node.right = TreeNode(0)
            stack.append((node.right, mid + 1, end))

    return root

# Helper function to test
from collections import deque
def treeToArray(root):
    if root is None:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        current = queue.popleft()
        if current is None:
            result.append(None)
            continue
        result.append(current.val)
        queue.append(current.left)
        queue.append(current.right)
    
    # Remove trailing None values to clean up the list representation
    while result and result[-1] is None:
        result.pop()
    
    return result


print(treeToArray(sortedArrayToBSTIterative([-10,-3,0,5,9])))
