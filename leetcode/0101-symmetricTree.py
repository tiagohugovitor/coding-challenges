# 0101-symmetricTree.py
# Problem: Symmetric Tree
# Link: https://leetcode.com/problems/symmetric-tree/description/
# Solved on: 2024-07-29

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time complexity: O(n)
# Space complexity: O(n)
# Description: This function checks if a binary tree is symmetric around its center.
# It defines a helper function `symmetricTree` that recursively compares the left and right
# subtrees. If the values of the nodes are equal and the subtrees are symmetric, the tree is symmetric.
# The base cases handle null nodes, ensuring both subtrees are null or both are not null.

def isSymmetricRecursive(root):
    if root is None:
        return True
    
    def symmetricTree(left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        else:
            return left.val == right.val and symmetricTree(left.left, right.right) and symmetricTree(left.right, right.left)

    return symmetricTree(root.left, root.right)

from collections import deque

# Time complexity: O(n)
# Space complexity: O(n)
# Description: This function checks if a binary tree is symmetric around its center using an iterative approach.
# It uses two queues to traverse the left and right subtrees simultaneously. The nodes are compared level by level.
# If all corresponding nodes in the left and right subtrees match, the tree is symmetric.

def isSymmetricIterative(root):
    if root is None:
        return True

    rightQueue = deque()
    leftQueue = deque()
    rightQueue.append(root.right)
    leftQueue.append(root.left)
    while rightQueue and leftQueue:
        left = leftQueue.popleft()
        right = rightQueue.popleft()
        if left is None and right is None:
            continue
        elif left is None or right is None:
            return False
        elif left.val == right.val:
            leftQueue.append(left.left)
            rightQueue.append(right.right)
            leftQueue.append(left.right)
            rightQueue.append(right.left)
        else:
            return False

    return len(leftQueue) == 0 and len(rightQueue) == 0

tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))

print(isSymmetricIterative(tree))
