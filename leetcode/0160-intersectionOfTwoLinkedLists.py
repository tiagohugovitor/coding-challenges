# 0160-intersectionOfTwoLinkedLists.py
# Problem: Intersection of Two Linked Lists
# Link: https://leetcode.com/problems/intersection-of-two-linked-lists/description/
# Solved on: 2024-07-31

# Time complexity: O(m + n)
# Space complexity: O(1)
# Description: This function finds the intersection node of two singly linked lists, if it exists.
# It uses two pointers to traverse both lists. If a pointer reaches the end of a list, it starts
# traversing the other list. This ensures that both pointers travel the same total distance,
# allowing them to meet at the intersection node or end up at None if there's no intersection.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getIntersectionNode(headA, headB):
    firstPointer = headA
    secondPointer = headB
    reachEnd = 0

    while (firstPointer and secondPointer) or reachEnd < 2:
        if firstPointer == None:
            firstPointer = headB
            reachEnd += 1
        if secondPointer == None:
            secondPointer = headA
            reachEnd += 1
        if firstPointer == secondPointer:
            return firstPointer
        else:
            firstPointer = firstPointer.next
            secondPointer = secondPointer.next
    
    return None

# Helper function to test
def createLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def getNodeAt(head, index):
    current = head
    while index > 0 and current:
        current = current.next
        index -= 1
    return current

def createIntersection(headA, headB, indexA):
    intersectNode = getNodeAt(headA, indexA)
    if intersectNode:
        tailB = headB
        while tailB.next:
            tailB = tailB.next
        tailB.next = intersectNode

listA = createLinkedList([4, 1, 8, 4, 5])
listB = createLinkedList([5, 0, 1])
createIntersection(listA, listB, 2)

def linkedListToList(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

intersectionNode = getIntersectionNode(listA, listB)
print(linkedListToList(getIntersectionNode(listA, listB)))
