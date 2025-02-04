import { createListFromArray, printList, Node } from "./2.0 - linkedListUtils.js"

const sumListsReverse = function (listA, listB) {
    let pointerA = listA
    let pointerB = listB
    const result = new Node(0, null)
    let current = result
    let carry = 0

    while (pointerA !== null && pointerB !== null) {
        const sum = pointerA.value + pointerB.value + carry
        carry = parseInt(sum / 10)
        const value = sum % 10 
        const newNode = new Node(value, null)
        current.next = newNode
        current = current.next
        pointerA = pointerA.next
        pointerB = pointerB.next
    }

    while (pointerA !== null) {
        const sum = pointerA.value + carry
        carry = parseInt(sum / 10)
        const value = sum % 10 
        const newNode = new Node(value, null)
        current.next = newNode
        current = current.next
        pointerA = pointerA.next
    }

    while (pointerB !== null) {
        const sum = pointerB.value + carry
        carry = parseInt(sum / 10)
        const value = sum % 10 
        const newNode = new Node(value, null)
        current.next = newNode
        current = current.next
        pointerB = pointerB.next
    }

    if (carry > 0) {
        const lastNode = new Node(carry, null)
        current.next = lastNode
    }

    return result.next
}

const sumListInOrder = function (listA, listB) {
    let pointerA = listA
    let pointerB = listB

    let reversedListA = new Node(0, null)
    let reversedListB = new Node(0, null)

    while (pointerA !== null) {
        const newNode = new Node(pointerA.value, reversedListA.next)
        reversedListA.next = newNode
        pointerA = pointerA.next
    }

    while (pointerB !== null) {
        const newNode = new Node(pointerB.value, reversedListB.next)
        reversedListB.next = newNode
        pointerB = pointerB.next
    }

    const resultReversed = sumListsReverse(reversedListA.next, reversedListB.next)
    let pointerResult = resultReversed
    const result = new Node(0, null)

    while (pointerResult !== null) {
        const newNode = new Node(pointerResult.value, result.next)
        result.next = newNode
        pointerResult = pointerResult.next
    }
    return result.next
}

const listA = createListFromArray([7,1,7])
const listB = createListFromArray([5,9,2])

printList(sumListsReverse(listA, listB))
printList(sumListInOrder(listA, listB))