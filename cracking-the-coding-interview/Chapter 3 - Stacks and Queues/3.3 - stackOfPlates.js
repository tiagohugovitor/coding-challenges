class SetOfStacks {
    constructor(threshold) {
        this.threshold = threshold
        this.stacks = []
    }

    push(value) {
        if (this.stacks.length && this.stacks[this.stacks.length - 1].length < this.threshold ) {
            this.stacks[this.stacks.length - 1].push(value)
        }
        else {
            this.stacks.push([value])
        }
    }

    pop() {
        if (!this.stacks.length) throw new Error('Empty Stack')
        const element = this.stacks[this.stacks.length - 1].pop()
        if (!this.stacks[this.stacks.length -1].length) {
            this.stacks.pop()
        }
        return element
    }

    popFromStack(stackIndex) {
        if (this.stacks.length < stackIndex) throw new Error('Empty Stack')
        const element = this.stacks[stackIndex - 1].pop()
        for(let i=stackIndex; i < this.stacks.length; i++) {
            this.stacks[i - 1].push(this.stacks[i][0])
            this.stacks[i].splice(0, 1)
        }
        return element
    }
}

const stacks = new SetOfStacks(3)
stacks.push(1)
stacks.push(1)
stacks.push(1)
stacks.push(2)
stacks.push(2)
stacks.push(2)
stacks.push(3)
stacks.push(3)
stacks.push(3)
stacks.push(4)
stacks.push(4)
console.log('Stack', stacks.stacks)
console.log('Removed top of stacks', stacks.pop())
stacks.pop()
stacks.pop()
console.log('Stack', stacks.stacks)
console.log('Removed from stack 2', stacks.popFromStack(2))
console.log('Stack', stacks.stacks)