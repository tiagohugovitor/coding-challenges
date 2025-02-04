import { MyStack } from "./3.0 - stackAndQueuesUtils.js"

const sortStack = (stack) => {
    const orderedStack = new MyStack
    while (!stack.isEmptyStack()) {
        const element = stack.popFromStack()
        while (!orderedStack.isEmptyStack() && orderedStack.peekFromStack() > element) {
            const smallerElement = orderedStack.popFromStack()
            stack.pushIntoStack(smallerElement)
        }
        orderedStack.pushIntoStack(element)
    }

    while(!orderedStack.isEmptyStack()) {
        const element = orderedStack.popFromStack()
        stack.pushIntoStack(element)
    }

    return stack
}

const stack = new MyStack()
stack.pushIntoStack(1)
stack.pushIntoStack(2)
stack.pushIntoStack(8)
stack.pushIntoStack(7)
stack.pushIntoStack(5)
stack.pushIntoStack(2)
stack.pushIntoStack(10)

console.log(sortStack(stack))