# 0024-swapNodesInPairs.py
# Problem: Swap Nodes in Pairs
# Link: https://leetcode.com/problems/swap-nodes-in-pairs/description/
# Solved on: 2024-07-22

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time complexity: O(n), where n is the number of nodes in the linked list.
# Space complexity: O(1)
# Description: This function swaps every two adjacent nodes in a singly linked list. It uses a dummy node (`newList`)
# to simplify the manipulation of the head of the list. The algorithm iterates through the list in pairs, for each pair,
# it updates the pointers to swap the positions of the two nodes. The process continues until all pairs are swapped, and
# the function returns the new head of the list.

def swapPairs(head):
    newList = ListNode(0)
    newList.next = head
    current = newList
    first = head
    second = head.next if head != None else None
    while first and second:
        current.next = second
        first.next = second.next
        second.next = first
        current = first
        first = first.next
        second = first.next if first != None else None

    return newList.next

#Auxiliary functions to run tests
def arrayToList(array):
    if not array:
        return None
    head = ListNode(array[0])
    current = head
    for value in array[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def listToArray(listNode):
    array = []
    while listNode:
        array.append(listNode.val)
        listNode = listNode.next
    return array

def printList(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(" -> ".join(map(str, result)) + " -> None")

printList(swapPairs(arrayToList([1, 2, 3, 4])))
