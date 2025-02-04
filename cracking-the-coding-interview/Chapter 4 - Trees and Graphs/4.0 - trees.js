class Tree {
    constructor() {
        this.root = null
    }
}

class Node {
    constructor() {
        this.value = 0
        this.right = null
        this.left = null
    }
}

const inOrderTraversal = (root) => {
    if (root == null) return
    inOrderTraversal(root.left)
    print(root.value)
    inOrderTraversal(root.right)
}

const preOrderTraversal = (root) => {
    if (root == null) return
    print(root.value)
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)
}

const postOrderTraversal = (root) => {
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.value)
}
