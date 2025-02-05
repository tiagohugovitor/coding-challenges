export class Tree {
    constructor() {
        this.root = null
    }
}

export class Node {
    constructor(value) {
        this.value = value
        this.right = null
        this.left = null
    }
}

export const inOrderTraversal = (root) => {
    if (root == null) return
    inOrderTraversal(root.left)
    console.log(root.value)
    inOrderTraversal(root.right)
}

export const preOrderTraversal = (root) => {
    if (root == null) return
    console.log(root.value)
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)
}

export const postOrderTraversal = (root) => {
    if (root == null) return
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    console.log(root.value)
}
