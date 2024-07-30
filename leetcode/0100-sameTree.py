# 0100-sameTree.py
# Problem: Same Tree
# Link: https://leetcode.com/problems/same-tree/description/
# Solved on: 2024-07-22

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time complexity: O(n)
# Space complexity: O(h)
# Description: This function checks if two binary trees are identical using a recursive approach.
# It compares the values of corresponding nodes and recursively checks the left and right subtrees.
# If all corresponding nodes have the same value and structure, the trees are identical.

def isSameTreeRecursive(firstTree, secondTree):
    if not firstTree and not secondTree:
        return True
    
    if not firstTree or not secondTree:
        return False
    
    if firstTree.val != secondTree.val:
        return False
    
    return isSameTreeRecursive(firstTree.left, secondTree.left) and isSameTreeRecursive(firstTree.right, secondTree.right)

from collections import deque

# Time complexity: O(n)
# Space complexity: O(n)
# Description: This function checks if two binary trees are identical using an iterative approach.
# It uses two queues to traverse both trees simultaneously. The nodes are compared level by level.
# If all corresponding nodes have the same value and structure, the trees are identical.

def isSameTreeIterative(firstTree, secondTree):
    firstTreeQueue = deque()
    secondTreeQueue = deque()
    firstTreeQueue.append(firstTree)
    secondTreeQueue.append(secondTree)

    while firstTreeQueue and secondTreeQueue:
        firstNode = firstTreeQueue.popleft()
        secondNode = secondTreeQueue.popleft()
        if not firstNode and not secondNode:
            continue
        elif not firstNode or not secondNode:
            return False
        elif firstNode.val != secondNode.val:
            return False
        else:
            firstTreeQueue.append(firstNode.left)
            secondTreeQueue.append(secondNode.left)
            firstTreeQueue.append(firstNode.right)
            secondTreeQueue.append(secondNode.right)
    
    return not firstTreeQueue and not secondTreeQueue


tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
tree2 = TreeNode(1, TreeNode(2), TreeNode(3))

print(isSameTreeRecursive(tree1, tree2))
