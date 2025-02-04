class MyQueue {
    constructor() {
        this.stackNewest = []
        this.stackOldest = []
    }

    size = () => {
        return this.stackNewest.length + this.stackOldest.length
    }

    shiftStacks = () => {
        if (!this.size()) throw new Error('Empty Queue')

        if (!this.stackOldest.length) {
            while (this.stackNewest.length) {
                const popElement = this.stackNewest.pop()
                this.stackOldest.push(popElement)
            }
        }
    }

    enqueue = (value) => {
        this.stackNewest.push(value)
    }

    dequeue = () => {
        this.shiftStacks()
        const element = this.stackOldest.pop()
        return element
    }

    peek = () => {
        this.shiftStacks()
        const element = this.stackOldest[this.stackOldest.length - 1]
        return element
    }
}


const queue = new MyQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
console.log('Queue', queue.stackNewest)
console.log('Queue', queue.stackOldest)
console.log('Dequeue', queue.dequeue())
console.log('Peek', queue.peek())
queue.enqueue(8)
console.log('Dequeue', queue.dequeue())