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
    let pointer = head;
    const array = [];
    
    while (pointer) {
        if (typeof pointer.value === "object" && pointer.value !== null) {
            array.push(JSON.stringify(pointer.value, null, 2));
        } else {
            array.push(pointer.value);
        }
        pointer = pointer.next;
    }
    
    console.log(array.join(" -> ") + " -> Null");
};

export const createIntersectedList = function (array, intersectIndex) {
    if (intersectIndex >= array.length) {
        throw new Error("Intersect index greater than array size")
    }
    
    const listAHead = new Node(0, null) 
    const listBHead = new Node(0, null)
    let pointerA = listAHead
    let pointerB = listBHead
    
    for(let i=0; i<intersectIndex; i++) {
        const newANode = new Node(array[i],null)
        const newBNode = new Node(array[i],null)
        pointerA.next = newANode
        pointerA = pointerA.next
        pointerB.next = newBNode
        pointerB = pointerB.next
    }

    for(let i=intersectIndex; i<array.length; i++) {
        const newNode = new Node(array[i],null)
        pointerA.next = newNode
        pointerA = pointerA.next
        pointerB.next = newNode
        pointerB = pointerB.next
    }

    return [listAHead.next, listBHead.next]
}

export const createLoop = function(listHead, cycleIndex) {
    let lastNode = listHead
    let cycleNode = listHead

    if (!listHead) throw new Error('Empty list')

    while(lastNode.next !== null) {
        lastNode = lastNode.next
    }

    for(let i=0; i<cycleIndex - 1; i++) {
        cycleNode = cycleNode.next
    }

    lastNode.next = cycleNode

    return listHead
}
