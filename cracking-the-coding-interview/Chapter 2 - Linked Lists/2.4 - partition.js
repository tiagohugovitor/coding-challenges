import { createListFromArray, Node, printList } from "./2.0 - linkedListUtils.js"

const partition = function (listHead, partitionValue) {
    if (!listHead) return null;

    let leftPointer = new Node(0, listHead)
    let rightPointer = listHead

    if (listHead.value < partitionValue) {
        leftPointer = leftPointer.next
    }

    while (rightPointer.next !== null) {
        if (rightPointer.next.value < partitionValue) {
            let auxiliar = rightPointer.next
            rightPointer.next = auxiliar.next
            auxiliar.next = leftPointer.next
            leftPointer.next = auxiliar
            leftPointer = leftPointer.next
        } else {
            rightPointer = rightPointer.next
        }
    }

    return listHead
}

const list = createListFromArray([5, 11, 12, 6, 9, 7, 10])
printList(partition(list, 10))