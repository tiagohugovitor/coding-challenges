# 0110-balancedBinaryTree.py
# Balanced Binary Tree
# Link: https://leetcode.com/problems/balanced-binary-tree/description/
# Solved on: 2024-07-30

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time complexity: O(n)
# Space complexity: O(h), where h is the height of the tree (due to recursion stack)
# Description: This function checks if a binary tree is height-balanced using a recursive approach.
# It recursively calculates the depth of each subtree and determines if the tree is balanced at each node.
# The tree is considered balanced if for every node, the difference between the heights of the left and right subtrees is no more than 1.

def isBalanced(root):
    def checkBalanceAndDepth(node):
        if not node:
            return True, 0
        
        balancedLeft, leftDepth = checkBalanceAndDepth(node.left)
        balancedRight, rightDepth = checkBalanceAndDepth(node.right)
        
        balanced = balancedLeft and balancedRight and abs(leftDepth - rightDepth) <= 1
        depth = max(leftDepth, rightDepth) + 1
        
        return balanced, depth
    
    balanced, _ = checkBalanceAndDepth(root)
    return balanced

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

print(isBalanced(arrayToTree([1,None,2,None,3])))
