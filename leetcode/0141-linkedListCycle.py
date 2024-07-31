# 0141-linkedListCycle.py
# Problem: Linked List Cycle
# Link: https://leetcode.com/problems/linked-list-cycle/description/
# Solved on: 2024-07-31

# Time complexity: O(n)
# Space complexity: O(1)
# Description: This function checks if a singly linked list has a cycle using the two-pointer (tortoise and hare) technique.
# It employs two pointers, `slowPointer` and `fastPointer`, which traverse the list at different speeds.
# If the list has a cycle, these pointers will eventually meet; otherwise, one of the pointers will reach the end of the list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    if head is None:
        return False

    slowPointer = head
    fastPointer = head.next

    while slowPointer and fastPointer:
        if slowPointer == fastPointer:
            return True
        slowPointer = slowPointer.next
        fastPointer = None if fastPointer.next is None else fastPointer.next.next 

    return False

# Helper function to test
def createCycleLinkedList(values, pos):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    cycleNode = None
    for i, value in enumerate(values[1:], 1):
        current.next = ListNode(value)
        current = current.next
        if i == pos:
            cycleNode = current
    current.next = cycleNode
    return head

print(hasCycle(createCycleLinkedList([1, 1, 2, 3, 5], 2)))
