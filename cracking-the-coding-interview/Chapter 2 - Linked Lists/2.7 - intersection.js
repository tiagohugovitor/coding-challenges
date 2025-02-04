import { createIntersectedList, printList } from "./2.0 - linkedListUtils.js"

const intersection = function (listA, listB) {
    let listASize = 0
    let listBSize = 0
    let pointerA = listA
    let pointerB = listB

    while (pointerA !== null) {
        listASize += 1
        pointerA = pointerA.next
    }

    while (pointerB !== null) {
        listBSize += 1
        pointerB = pointerB.next
    }

    pointerA = listA
    pointerB = listB
    const sizeDifference = Math.abs(listASize - listBSize)

    if (listASize > listBSize) {
        for(let i=0; i<sizeDifference; i++) {
            pointerA = pointerA.next
        }
    }

    else {
        for(let i=0; i<sizeDifference; i++) {
            pointerB = pointerB.next
        }
    }

    while (pointerA !== pointerB) {
        pointerA = pointerA.next
        pointerB = pointerB.next
    }

    return pointerA
}

const [listA, listB] = createIntersectedList([1,2,3,4,5,6,7], 3)
console.log(printList(intersection(listA, listB)))
