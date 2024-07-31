# 0104-maximumDepthOfBinaryTree.py
# Problem: Maximum Depth of Binary Tree
# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Solved on: 2024-07-29

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time complexity: O(n)
# Space complexity: O(h)
# Description: This function calculates the maximum depth of a binary tree using a recursive approach.
# It defines an inner helper function `calculateMaxDepth` which recursively computes the depth of the left and right subtrees.
# The function returns the maximum depth from the root to the deepest leaf node.

def maxDepthRecursive(root):
    if root is None:
        return 0
    
    def calculateMaxDepth(node):
        if node is None:
            return 0
        return 1 + max(calculateMaxDepth(node.right), calculateMaxDepth(node.left))

    return calculateMaxDepth(root)

# Time complexity: O(n)
# Space complexity: O(n)
# Description: This function calculates the maximum depth of a binary tree using an iterative BFS approach.
# It uses a queue to traverse the tree level by level and keeps track of the maximum depth encountered. 
# The function returns the maximum depth from the root to the furthest leaf node.

from collections import deque
def maxDepthIterative(root):
    if root is None:
        return 0
    
    queue = deque([(root, 1)])
    maxDepth = 1

    while queue:
        current, depth = queue.popleft()
        if current is not None:
            maxDepth = max(maxDepth, depth)
            queue.append((current.left, depth + 1))
            queue.append((current.right, depth + 1))

    return maxDepth


tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

print(maxDepthRecursive(tree))
