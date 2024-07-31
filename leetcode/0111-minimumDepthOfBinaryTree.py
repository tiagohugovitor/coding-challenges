# 0111-minimumDepthOfBinaryTree.py
# Problem: Minimum Depth of Binary Tree
# Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
# Solved on: 2024-07-30

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time complexity: O(n)
# Space complexity: O(h)
# Description: This function calculates the minimum depth of a binary tree using a recursive approach.
# It defines an inner helper function `calculateMinDepth` which recursively computes the depth of the left and right subtrees.
# The function returns the minimum depth from the root to the nearest leaf node.

def minDepthRecursive(root):
    if root == None:
        return 0
    
    def calculateMinDepth(node):
        if node.left is None and node.right is None:
            return 1
        if node.left is None:
            return 1 + calculateMinDepth(node.right)
        if node.right is None:
            return 1 + calculateMinDepth(node.left)
        return 1 + min(calculateMinDepth(node.right), calculateMinDepth(node.left))
    
    return calculateMinDepth(root)

# Time complexity: O(n)
# Space complexity: O(n)
# Description: This function calculates the minimum depth of a binary tree using an iterative BFS approach.
# It uses a queue to traverse the tree level by level. The function returns the minimum depth from the root to the nearest leaf node.

from collections import deque
def minDepthIterative(root):
    if root is None:
        return 0

    queue = deque([(root, 1)])

    while queue:
        current, depth = queue.popleft()
        if current is None:
            continue
        elif current.left == None and current.right == None:
            return depth
        else:
            queue.append((current.left, depth + 1))
            queue.append((current.right, depth + 1))

    return -1

# Helper functions to test
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

print(minDepthIterative(arrayToTree([2,None,3,None,4,None,5,None,6])))
