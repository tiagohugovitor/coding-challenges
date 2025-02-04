import { printList } from "../Chapter 2 - Linked Lists/2.0 - linkedListUtils.js"

class Node {
    constructor(value, next) {
        this.value = value
        this.next = next
    }
}

class LinkedList {
    constructor() {
        this.head = null
        this.tail = null
    }

    enqueue = (value) => {
        const newNode = new Node(value)
        if (this.tail === null) {
            this.head = newNode
            this.tail = newNode
        }
        else {
            this.tail.next = newNode
            this.tail = newNode
        }
    }

    dequeue = () => {
        if (this.head === null) throw new Error('Empty Queue')
        const element = this.head
        this.head = this.head.next
        if (this.head === null) {
            this.tail = null
        }
        return element.value
    }

    peek = () => {
        if (this.head === null) return null
        return this.head.value        
    }
}


class Animal {
    constructor(type, name, order) {
        this.type = type
        this.name = name
        this.order = order
    }

    isOlderThan = (animal) => {
        return this.order < animal.order
    }
}
class Cat extends Animal {
    constructor(name, order) {
        super('cat', name, order);
    }
}

class Dog extends Animal {
    constructor(name, order) {
        super('dog', name, order);
    }
}

class AnimalShelder {
    constructor() {
        this.cat = new LinkedList()
        this.dog = new LinkedList()
        this.order = 0
    }

    enqueueAnimal = (name, type) => {
        this.order += 1
        if (type === 'dog') {
            const newAnimal = new Dog(name, this.order)
            this.dog.enqueue(newAnimal)
        }
        else {
            const newAnimal = new Cat(name, this.order)
            this.cat.enqueue(newAnimal)   
        }
    }

    dequeueDog = () => {
        return this.dog.dequeue()
    }

    dequeueCat = () => {
        return this.cat.dequeue()
    }

    dequeueAny = () => {
        const cat = this.cat.peek()
        const dog = this.dog.peek()

        if (dog === null && cat === null) throw new Error('Empty Shelder')

        if (cat !== null && cat.isOlderThan(dog)) {
            return this.dequeueCat()
        }
        return this.dequeueDog()
    }
}

const shelder = new AnimalShelder()
shelder.enqueueAnimal('A','dog')
shelder.enqueueAnimal('B','cat')
shelder.enqueueAnimal('C','dog')
shelder.enqueueAnimal('D','cat')
shelder.enqueueAnimal('E','cat')
shelder.enqueueAnimal('F','cat')
shelder.enqueueAnimal('G','dog')

printList(shelder.dog.head)
console.log('--------------------------')
printList(shelder.cat.head)

console.log('--------------------------')

shelder.dequeueDog()

console.log('--------------------------')

printList(shelder.dog.head)
console.log('--------------------------')
printList(shelder.cat.head)


console.log('--------------------------')

shelder.dequeueCat()

console.log('--------------------------')

printList(shelder.dog.head)
console.log('--------------------------')
printList(shelder.cat.head)

shelder.dequeueAny()
shelder.dequeueAny()
shelder.dequeueAny()

console.log('--------------------------')

printList(shelder.dog.head)
console.log('--------------------------')
printList(shelder.cat.head)

console.log('--------------------------')