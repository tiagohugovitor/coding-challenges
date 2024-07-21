# 0019-removeNodeFromEndOfList.py
# Problem: Remove Nth Node From End of List
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Solved on: 2024-07-21

# Time complexity: O(n)
# Space complexity: O(1)
# Description This function removes the nth node from the end of a singly linked list.
# It first iterates through the list to find the nth node from the end, then adjusts the pointers
# to exclude the target node from the list. The function handles edge cases such as removing the
# head of the list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    temp = head
    previous = head
    while temp:
        nth = temp
        for _ in range(n):
            nth = nth.next
        if nth == None:
            if(temp == head):
                head = head.next
                break             
            previous.next = temp.next
            temp.next = None
            break
        temp = temp.next
        if previous.next != temp:
            previous = previous.next

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

head = createLinkedList([1, 2, 3, 4, 5])

print('Before removal', linkedListToList(head))

new_head = removeNthFromEnd(head, 2)

print('After removal', linkedListToList(new_head))
