# 0145-binaryTreePostorderTraversal.py
# Problem: Binary Tree Postorder Traversal
# Link: https://leetcode.com/problems/binary-tree-postorder-traversal/description/
# Solved on: 2024-07-25

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time complexity: O(n)
# Space complexity: O(h)
# Description: This function performs a postorder traversal of a binary tree using a recursive approach. 
# In postorder traversal, nodes are visited in this order: left subtree, right subtree, root.
# The function recursively traverses the left and right subtrees before appending the root node's value to the result list.
# This ensures that nodes are processed in the correct postorder sequence.

def postorderTraversalRecursive(root):
    result = []
    def postorder(node, result):
        if node is not None:
            postorder(node.left, result)
            postorder(node.right, result)
            result.append(node.val)
        
    postorder(root, result)
    return result

# Time complexity: O(n)
# Space complexity: O(h)
# Description: This function performs a postorder traversal of a binary tree using an iterative approach with a stack. 
# In postorder traversal, nodes are visited in this order: left subtree, right subtree, root.
# The function uses a stack to manage the nodes and a variable to keep track of the last visited node to ensure nodes are processed in the correct postorder sequence.

def postorderTraversalIterative(root):
    if not root:
        return []

    result = []
    current = root
    stack = []
    lastVisitedNode = None

    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            peekLast = stack[-1]
            if peekLast.right and lastVisitedNode != peekLast.right:
                current = peekLast.right
            else:
                result.append(peekLast.val)
                lastVisitedNode = stack.pop()

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

print(postorderTraversalRecursive(arrayToTree([1,None,2,3])))
