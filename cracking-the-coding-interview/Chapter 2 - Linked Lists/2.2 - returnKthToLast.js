import { createListFromArray, printList } from "./2.0 - linkedListUtils.js"

const returnKthToLast = function (head, k) {
    let leftPointer = head
    let rightPointer = head

    for (let i=0; i< k - 1; i++) {
        if (rightPointer === null) {
            console.log('List smaller than k')
            return head
        } 
        rightPointer = rightPointer.next
    }

    while (rightPointer.next !== null) {
        leftPointer = leftPointer.next
        rightPointer = rightPointer.next
    }

    return leftPointer
}

const list = createListFromArray([2,3,1,2,7])
printList(returnKthToLast(list, 3))