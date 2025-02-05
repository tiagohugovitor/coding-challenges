import { Node, inOrderTraversal, postOrderTraversal } from './4.0 - trees.js'

const minimalTree = (array, start, end) => {
    if (start > end) return null

    const rootIndex = Math.floor((start + end) / 2);
    const root = new Node(array[rootIndex])
    root.left = minimalTree(array, start, rootIndex - 1)
    root.right = minimalTree(array, rootIndex + 1, end)

    return root
}

const tree = minimalTree([1,3,5,6,7], 0, 4)
console.log("In-Order Traversal:");
inOrderTraversal(tree);

console.log("Post-Order Traversal:");
postOrderTraversal(tree);