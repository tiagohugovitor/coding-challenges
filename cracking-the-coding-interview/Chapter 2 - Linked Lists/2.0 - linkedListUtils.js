export class Node {
    constructor(x, next=null) {
        this.value = x;
        this.next = next;
    }
}

export const createListFromArray = function (array) {
    const head = new Node(0);
    let pointer = head;
    for (const value of array) {
        const newNode = new Node(value, null)
        pointer.next = newNode
        pointer = pointer.next 
    }

    return head.next;
}

export const printList = function (head) {
    let pointer = head
    const array = []
    while(pointer !== null) {
        array.push(pointer.value)
        pointer = pointer.next
    }
    console.log(array.join(' -> ') + ' -> Null')
}
