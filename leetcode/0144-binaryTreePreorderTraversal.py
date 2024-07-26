# 0144-binaryTreePreorderTraversal.py
# Problem: Binary Tree Preorder Traversal
# Link: https://leetcode.com/problems/binary-tree-preorder-traversal/description/
# Solved on: 2024-07-25

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time complexity: O(n)
# Space complexity: O(n) in worst case
# Description: This function performs a preorder traversal of a binary tree using recursion. 
# In preorder traversal, the nodes are recursively visited in this order: root, left subtree, right subtree.
# The function appends the value of each node to the result list as it traverses the tree.

def preorderTraversalRecursive(root):
    result = []

    def preorderTraversal(node, result):
        if node is not None:
            result.append(node.val)
            preorderTraversal(node.left, result)
            preorderTraversal(node.right, result)

    preorderTraversal(root, result)
    return result

# Time complexity: O(n)
# Space complexity: O(n) in worst case
# Description: This function performs a preorder traversal of a binary tree using an iterative approach with a stack. 
# In preorder traversal, the nodes are visited in this order: root, left subtree, right subtree.
# The function uses a stack to keep track of nodes to visit next and appends the value of each node to the result list as it traverses the tree.

def preorderTraversalIterative(root):
    stack = []
    result = []
    current = root
    
    while stack or current:
        while current:
            stack.append(current)
            result.append(current.val)
            current = current.left
        current = stack.pop()
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

print(preorderTraversalIterative(arrayToTree([1,None,2,3])))
