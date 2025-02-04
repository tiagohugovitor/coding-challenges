import { createListFromArray, createLoop } from "./2.0 - linkedListUtils.js"

const loopDetection = function (listHead) {
    let slowPointer = listHead
    let fastPointer = listHead

    while (fastPointer !== null && fastPointer.next !== null) {
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next

        if (fastPointer === slowPointer) {
            break
        }
    }

    if (fastPointer === null || fastPointer.next === null) {
        throw new Error('List has no cycle')
    }

    slowPointer = listHead

    while(slowPointer !== fastPointer) {
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next
    }

    return slowPointer
}

const listA = createListFromArray([1,2,3,4,5,6])
createLoop(listA, 2)
const cycleIndex = loopDetection(listA)
console.log(cycleIndex.value)