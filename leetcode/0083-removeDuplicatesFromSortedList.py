# 0083-removeDuplicatesFromSortedList.py
# Problem: Remove Duplicates from Sorted List
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# Solved on: 2024-07-24

# Time complexity: O(n)
# Space complexity: O(1)
# Description: This function runs through the list once with two pointers removing duplicates.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeDuplicatesFromSortedList(head):
    previous = head
    current = head.next if head is not None else None

    while current is not None:
        if previous.val == current.val:
            previous.next = current.next
        else:
            previous = previous.next
        current = current.next

    return head

# Helper functions to test
def createLinkedList(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linkedListToList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

print(linkedListToList(removeDuplicatesFromSortedList(createLinkedList([1, 1, 2, 3, 5]))))
