# 0203-removeElements.py
# Problem: Remove Linked List Elements
# Link: https://leetcode.com/problems/remove-linked-list-elements/description/
# Solved on: 2024-08-14

# Time complexity: O(n)
# Space complexity: O(1)
# Description: This function removes all nodes with the value val from a singly
# linked list using a dummy head node. It iterates through the list, adjusting
# pointers to bypass nodes with the target value. The resulting list is returned,
# starting from the node after the dummy head.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val):
    newHead = ListNode()
    newHead.next = head
    previous = newHead
    current = head

    while current != None:
        if current.val == val:
            previous.next = current.next
        else:
            previous = previous.next    
        current = current.next

    return newHead.next

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

def printList(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(" -> ".join(map(str, result)) + " -> None")

printList(removeElements(arrayToList([4, 1, 2, 3, 4]), 4))