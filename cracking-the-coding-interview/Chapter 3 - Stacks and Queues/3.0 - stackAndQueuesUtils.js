// Melhor usando linked list. O(1) para inserção e remoção
export class MyQueue {
    constructor() {
        this.queue = []
    }

    enqueue (element) {
        this.queue.push(element)
    }
    
    dequeue () {
        if (this.isEmptyQueue()) throw new Error('Empty Queue')
        return this.queue.shift()
    }
    
    peekFromQueue () {
        if (this.isEmptyQueue()) throw new Error('Empty Queue')
        return this.queue[0]
    }
    
    isEmptyQueue () {
        return !this.queue.length
    }
}

export class MyStack {
    constructor() {
        this.stack = []
    }

    pushIntoStack (element) {
        this.stack.push(element)
    }
    
    popFromStack () {
        if(this.isEmptyStack()) throw new Error('Empty Stack')
        return this.stack.pop()
    }
    
    peekFromStack () {
        if(this.isEmptyStack()) throw new Error('Empty Stack')
        return this.stack[this.stack.length - 1]
    }
    
    isEmptyStack () {
        return !this.stack.length
    }
}

