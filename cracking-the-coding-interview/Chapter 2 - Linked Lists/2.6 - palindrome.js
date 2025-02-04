import { createListFromArray, Node } from "./2.0 - linkedListUtils.js"

const palindrome = function (listHead) {
    const reverseList = new Node(0, null)
    let current = listHead
    let currentReverse = reverseList

    while (current !== null) {
        const newNode = new Node(current.value, currentReverse.next)
        currentReverse.next = newNode
        current = current.next
    }

    current = listHead
    currentReverse = reverseList.next

    let isPalindrome = true
    while (current != null) {
        if (current.value !== currentReverse.value) {
            isPalindrome = false
            break
        }
        current = current.next
        currentReverse = currentReverse.next
    }
    return isPalindrome
}

const list = createListFromArray([])
console.log(palindrome(list))

const palindromeStack = function (headList) {
    let slowPointer = headList
    let fastPointer = headList

    let queue = []

    while (fastPointer !== null && fastPointer.next !== null) {
        queue.push(slowPointer.value)
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
    }

    if (fastPointer !== null) {
        slowPointer = slowPointer.next
    }

    while (slowPointer !== null) {
        const topElement = queue.pop()
        if(topElement !== slowPointer.value) {
            return false
        }
        slowPointer = slowPointer.next
    }

    return true
}


const listB = createListFromArray([1,2,3,2,1])
console.log(palindromeStack(listB))
