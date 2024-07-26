# 0112-pathSum.py
# Problem: Path Sum
# Link: https://leetcode.com/problems/path-sum/description/
# Solved on: 2024-07-25

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time complexity: O(n)
# Space complexity: O(h)
# Description: This function checks if there is a root-to-leaf path in a binary tree such that the sum of the values along the path equals a given target.
# The function uses a depth-first search (DFS) approach to traverse the tree recursively. It maintains the cumulative path sum as it traverses the tree,
# and checks if the path sum equals the target when a leaf node is reached. If a valid path is found, the function returns True; otherwise, it returns False.

def hasPathSumRecursive(root, target):
    def dfs(node, pathCost, target):
        if node is not None and node.left is None and node.right is None:
            if pathCost + node.val == target:
                return True
            else:
                return False
        if node is not None:
            return dfs(node.left, pathCost + node.val, target) or dfs(node.right, pathCost + node.val, target)

    return dfs(root, 0, target)

# Time complexity: O(n)
# Space complexity: O(h)
# Description: This function checks if there is a root-to-leaf path in a binary tree such that the sum of the values along the path equals a given target.
# The function uses an iterative depth-first search (DFS) approach with a stack. Each stack entry contains a node and the cumulative path sum up to that node.
# The algorithm traverses the tree, updating the path sum and checking if a leaf node's path sum equals the target. If a valid path is found, the function
# returns True; otherwise, it returns False.

def hasPathSumIterative(root, target):
    if not root:
        return False

    stack = [(root, root.val)]

    while stack:
        node, currentSum = stack.pop()
        if not node.left and not node.right:
            if currentSum == target:
                return True
        if node.right:
            stack.append((node.right, currentSum + node.right.val))
        if node.left:
            stack.append((node.left, currentSum + node.left.val))
    return False

# Helper functions to test

from collections import deque
def arrayToTree(arr):
    if not arr:
        return None
    
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < len(arr):
        current = queue.popleft()
        if arr[i] is not None:
            current.left = TreeNode(arr[i])
            queue.append(current.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            current.right = TreeNode(arr[i])
            queue.append(current.right)
        i += 1

    return root

print(hasPathSumIterative(arrayToTree([5,4,8,11,None,13,4,7,2,None,None,None,1]), 26))
