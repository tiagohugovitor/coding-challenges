import { createListFromArray, printList, Node } from './2.0 - linkedListUtils.js'

const removeDups = function(head) {
    let seen = new Set()
    let pointer = new Node
    pointer.next = head 

    while(pointer.next !== null) {
        if (seen.has(pointer.next.value)) {
            pointer.next = pointer.next.next
        }
        else {
            seen.add(pointer.next.value)
            pointer = pointer.next
        }
    }

    return head
}
const head = createListFromArray([2,3,1,2,3,5])
printList(removeDups(head))
