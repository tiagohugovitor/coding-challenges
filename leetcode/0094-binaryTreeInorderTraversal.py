# 0094-binaryTreeInorderTraversal.py
# Problem: Binary Tree Inorder Traversal
# Link: https://leetcode.com/problems/binary-tree-inorder-traversal/description/
# Solved on: 2024-07-24

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time complexity: O(n)
# Space complexity: O(h), where h is the height of the tree (due to the recursion stack)
# Description: This function performs an inorder traversal of a binary tree recursively.
# It traverses the left subtree, visits the root, and then traverses the right subtree.
# The result is a list of node values in inorder sequence.

def inorderTraversalRecursive(root):
    result = []

    def inorderTraversal(root, result):
        if root is not None:
            inorderTraversal(root.left, result)
            result.append(root.val)
            inorderTraversal(root.right, result)

    inorderTraversal(root, result)

    return result

# Time complexity: O(n)
# Space complexity: O(h), where h is the height of the tree (due to the stack)
# Description: This function performs an inorder traversal of a binary tree iteratively using a stack.
# It simulates the recursion by using a stack to traverse the left subtree, visit the root,
# and then traverse the right subtree. The result is a list of node values in inorder sequence.

def inorderTraversalIterative(root):
    stack = []
    result = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right
    
    return result

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

print(inorderTraversalIterative(arrayToTree([1,None,2,3])))
