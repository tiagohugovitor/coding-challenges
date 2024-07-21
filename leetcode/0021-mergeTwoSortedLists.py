# 0021-mergeTwoSortedLists.py
# Problem: Merge Two Sorted Lists
# Link: https://leetcode.com/problems/merge-two-sorted-lists/description/
# Solved on: 2024-07-21

# Time complexity: O(n + m), where n and m are the lengths of the two input lists.
# Space complexity: O(1), since we are only using a few extra pointers.
# Description: This function merges two sorted linked lists into one sorted linked list.
# It iteratively compares the elements of both lists, adding the smaller element to the new list.
# Once one of the lists is exhausted, the remaining elements of the other list are appended to the new list.
# The function handles edge cases where one or both input lists are empty.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoSortedLists(list1, list2):
    if list1 == None:
        return list2

    if list2 == None:
        return list1

    head = ListNode(0)
    newList = head
    temp1 = list1
    temp2 = list2

    while temp1 != None and temp2 != None:
        if temp1.val <= temp2.val:
            newList.next = temp1
            temp1 = temp1.next
        else:
            newList.next = temp2
            temp2 = temp2.next
        newList = newList.next

    if temp1 != None:
        newList.next = temp1
    
    if temp2 != None:
        newList.next = temp2

    return head.next


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

list1 = createLinkedList([1, 3, 5])
list2 = createLinkedList([2, 4, 6])

print('Before Merge', linkedListToList(list1), linkedListToList(list2))

newList = mergeTwoSortedLists(list1, list2)

print('After Merge', linkedListToList(newList))
