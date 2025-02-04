class ThreeInOne {
    constructor() {
        this.stack = []
        this.endFirstStack = 0
        this.startSecondStack = 0
        this.endSecondStack = 0
        this.startThirdStack = 0
    }

    pushFirstStack(value) {
        this.stack.splice(this.endFirstStack, 0, value);
        this.endFirstStack += 1
        this.startSecondStack += 1
        this.endSecondStack += 1
        this.startThirdStack += 1
    }

    popFirstStack() {
        if (this.endFirstStack === 0) throw new Error('First stack is empty')
        const element = this.stack.splice(this.endFirstStack - 1, 1)[0]
        this.endFirstStack -= 1
        this.startSecondStack -= 1
        this.endSecondStack -= 1
        this.startThirdStack -= 1
        return element
    }

    pushSecondStack(value) {
        this.stack.splice(this.endSecondStack, 0, value);
        this.endSecondStack += 1
        this.startThirdStack += 1
    }

    popSecondStack() {
        if (this.startSecondStack === this.endSecondStack) throw new Error('Second stack is empty')
        const element = this.stack.splice(this.endSecondStack - 1, 1)[0]
        this.endSecondStack -= 1
        this.startThirdStack -= 1
        return element
    }

    pushThirdStack(value) {
        this.stack.push(value)
    }

    popThirdStack() {
        if (this.startThirdStack === this.stack.length) throw new Error('Third stack is empty')
        return this.stack.pop()
    }

}
