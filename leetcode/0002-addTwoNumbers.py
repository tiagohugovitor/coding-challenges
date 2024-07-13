# 0002-addTwoNumbers.py
# Problem: Add Two Numbers
# Link: https://leetcode.com/problems/add-two-numbers/description/
# Solved on: 2024-07-13

# Time complexity: O(n + m).
# Description: This function adds two numbers represented by linked lists l1 and l2.
# Each node contains a single digit and the digits are stored in reverse order.
# The function returns the sum as a linked list in the same reverse order.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers( l1, l2):
    p = l1
    q = l2
    carry = 0
    val = (p.val + q.val) % 10
    if (p.val + q.val) >= 10:
        carry = 1
    else:
        carry = 0
    p = p.next
    q = q.next
    result = ListNode(val)
    current = result
    while p is not None and q is not None:
        val = (p.val + q.val + carry) % 10
        if (p.val + q.val + carry) >= 10:
            carry = 1
        else:
            carry = 0
        p = p.next
        q = q.next
        current.next = ListNode(val)
        current = current.next
    while p is not None:
        val = (p.val + carry) % 10
        if (p.val + carry) >= 10:
            carry = 1
        else:
            carry = 0
        p = p.next
        current.next = ListNode(val)
        current = current.next
    while q is not None:
        val = (q.val + carry) % 10
        if (q.val + carry) >= 10:
            carry = 1
        else:
            carry = 0
        q = q.next
        current.next = ListNode(val)
        current = current.next
    if carry == 1:
        current.next = ListNode(1)
        current = current.next
    return result

def createLinkedList(values):
    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head

def printLinkedList(node):
    while node is not None:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

printLinkedList(addTwoNumbers(createLinkedList([2,4,3]), createLinkedList([5,6,4])))