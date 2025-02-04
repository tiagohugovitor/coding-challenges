class MinStack {
    constructor () {
        this.stack = []
        this.minStack = []
    }

    pushToStack(value) {
        this.stack.push(value)
        if (!this.minStack.length || value <= this.minStack[this.minStack.length - 1]) {
            this.minStack.push(value)
        }
    }

    popFromStack() {
        if (!this.stack.length) throw new Error('Empty Stack')
        const element = this.stack.pop()
        if (element === this.minStack[this.minStack.length - 1]) {
            this.minStack.pop()
        }
        return element
    }

    minFromStack() {
        if (!this.stack.length) throw new Error('Empty Stack')
        return this.minStack[this.minStack.length - 1]
    }
}

const stackWithMin = new MinStack()

stackWithMin.pushToStack(5)
stackWithMin.pushToStack(4)
stackWithMin.pushToStack(3)
stackWithMin.pushToStack(3)
stackWithMin.pushToStack(2)

console.log(stackWithMin.minFromStack())

stackWithMin.popFromStack()
console.log(stackWithMin.minFromStack())

stackWithMin.popFromStack()
console.log(stackWithMin.minFromStack())

stackWithMin.popFromStack()
console.log(stackWithMin.minFromStack())