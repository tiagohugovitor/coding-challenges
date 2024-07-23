# 0023-mergeKSortedLists.py
# Problem: Merge k Sorted Lists
# Link: https://leetcode.com/problems/merge-k-sorted-lists/description/
# Solved on: 2024-07-22

# Time complexity: O(4^n / sqrt(n)), n-th Catalan number
# Space complexity: O(4^n / sqrt(n))
# Description: This function generates all combinations of `n` pairs of valid parentheses.
# It uses a recursive helper function `generate` that builds the combinations by adding open and close parentheses
# while maintaining the validity of the sequences. The function ensures that the number of open parentheses 
# never exceeds `n` and that the number of close parentheses never exceeds the number of open parentheses.
# The resulting combinations are stored in the `result` list, which is returned at the end.

import sys
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time complexity: O(nk^2), where n is the total number of nodes and k is the number of linked lists.
# Space complexity: O(1)
# Description: This function merges k sorted linked lists into one sorted linked list using a brute force approach.
# The algorithm repeatedly finds the minimum element from the heads of the lists and appends it to the result list.
# It adjusts the lists by removing empty lists from consideration. The main disadvantage of this approach is its
# inefficiency, especially for large values of k, as it requires scanning all lists to find the minimum value at each step.
    
def mergeKListsBruteForce(lists):
        k = len(lists)
        head = ListNode(0, None)
        current = head

        while k > 0:
            minValue = float('inf')
            minPointer = 0
            for i in range(k):
                if lists[i] == None:
                    lists[k-1], lists[i] = lists[i], lists[k-1]
                    k -= 1
                    minPointer = -1
                    break
                elif lists[i].val < minValue:
                    minPointer = i
                    minValue = lists[i].val
            if minPointer != -1 and lists[minPointer] != None:
                current.next = lists[minPointer]
                current = current.next
                lists[minPointer] = lists[minPointer].next

        return head.next


# Time complexity: O(nlogk), where n is the total number of nodes and k is the number of linked lists.
# Space complexity: O(k)
# Description: This function merges k sorted linked lists into one sorted linked list using a min-heap (priority queue).
# The algorithm initializes the heap with the head nodes of all non-empty lists. It then repeatedly extracts the minimum
# element from the heap, appends it to the result list, and inserts the next element from the same list into the heap.
# This approach significantly improves efficiency by reducing the time complexity to O(nlogk), making it more suitable
# for large values of k.
    
def mergeKListsHeap(lists):
    heap = []

    for i in range(len(lists)):
        if lists[i] != None:
            heapq.heappush(heap, (lists[i].val, i))

    head = ListNode(0)
    current = head

    while heap:
        _, i = heapq.heappop(heap)
        current.next = lists[i]
        current = current.next
        lists[i] = lists[i].next
        if lists[i] != None:
            heapq.heappush(heap, (lists[i].val, i))

    return head.next

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

lists = [arrayToList([1, 4, 5]), arrayToList([1, 3, 4]), arrayToList([2, 6])]
printList(mergeKListsHeap(lists))