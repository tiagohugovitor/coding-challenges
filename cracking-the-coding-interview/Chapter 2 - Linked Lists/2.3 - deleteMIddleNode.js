import { createListFromArray, printList } from "./2.0 - linkedListUtils.js"

const deleteMiddleNode = function (listHead, nodeValue) {
    let pointer = listHead

    while (pointer.next.value !== nodeValue) {
        pointer = pointer.next
    }

    pointer.next = pointer.next.next

    return listHead
}

const list = createListFromArray([1,2,3,10,4,5])
printList(deleteMiddleNode(list, 10))

const deleteMiddleNodeWithoutHead = function (nodeValue) {

    nodeValue.value = nodeValue.next.value
    nodeValue.next = nodeValue.next.next

    return nodeValue
}

const listB = createListFromArray([1,2,3,10,4,5])
deleteMiddleNodeWithoutHead(listB.next.next.next)
printList(listB)
