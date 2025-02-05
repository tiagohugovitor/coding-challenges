class Node {
    constructor(value) {
        this.value = value
        this.left = null
        this.right = null
        this.parent = null
    }
}

class minHeap {
    constructor() {
        this.root = null
        this.nodes = []
    }

    insert = (value) => {
        const newNode = new Node(value)
        if (!this.root) {
            this.root = newNode
        }
        else {
            let parent = this.nodes[Math.floor((this.nodes.length - 1)/2)]
            if (!parent.left) {
                parent.left = newNode
            } else {
                parent.right = newNode
            }
            newNode.parent = parent
            this.heapifyUp(newNode)
        }
        this.nodes.push(newNode);
    }

    extractMin() {
        if (!this.root) return null;
        if (this.nodes.length === 1) {
            const min = this.root.value;
            this.root = null;
            this.nodes = [];
            return min;
        }

        const min = this.root.value;
        const lastNode = this.nodes.pop();

        if (this.nodes.length > 0) {
            this.root.value = lastNode.value;
            this.replaceNode(lastNode, this.root);
            this.heapifyDown(this.root);
        }

        return min;
    }

    heapifyUp(node) {
        while (node.parent && node.value < node.parent.value) {
            [node.value, node.parent.value] = [node.parent.value, node.value];
            node = node.parent;
        }
    }

    heapifyDown(node) {
        while (node.left || node.right) {
            let smallest = node;
            if (node.left && node.left.value < smallest.value) {
                smallest = node.left;
            }
            if (node.right && node.right.value < smallest.value) {
                smallest = node.right;
            }
            if (smallest === node) break;

            [node.value, smallest.value] = [smallest.value, node.value];
            node = smallest;
        }
    }

    replaceNode(oldNode, newNode) {
        if (oldNode.parent) {
            if (oldNode.parent.left === oldNode) {
                oldNode.parent.left = newNode;
            } else {
                oldNode.parent.right = newNode;
            }
        }
        newNode.parent = oldNode.parent;
    }
}

class MaxHeap {
    constructor() {
        this.root = null;
        this.nodes = [];
    }

    insert(value) {
        const newNode = new Node(value);
        if (!this.root) {
            this.root = newNode;
        } else {
            let parent = this.nodes[Math.floor((this.nodes.length - 1) / 2)];
            if (!parent.left) {
                parent.left = newNode;
            } else {
                parent.right = newNode;
            }
            newNode.parent = parent;
            this.heapifyUp(newNode);
        }
        this.nodes.push(newNode);
    }

    extractMax() {
        if (!this.root) return null;
        if (this.nodes.length === 1) {
            const max = this.root.value;
            this.root = null;
            this.nodes = [];
            return max;
        }

        const max = this.root.value;
        const lastNode = this.nodes.pop();

        if (this.nodes.length > 0) {
            this.root.value = lastNode.value;
            this.replaceNode(lastNode, this.root);
            this.heapifyDown(this.root);
        }

        return max;
    }

    heapifyUp(node) {
        while (node.parent && node.value > node.parent.value) {
            [node.value, node.parent.value] = [node.parent.value, node.value];
            node = node.parent;
        }
    }

    heapifyDown(node) {
        while (node.left || node.right) {
            let largest = node;
            if (node.left && node.left.value > largest.value) {
                largest = node.left;
            }
            if (node.right && node.right.value > largest.value) {
                largest = node.right;
            }
            if (largest === node) break;

            [node.value, largest.value] = [largest.value, node.value];
            node = largest;
        }
    }

    replaceNode(oldNode, newNode) {
        if (oldNode.parent) {
            if (oldNode.parent.left === oldNode) {
                oldNode.parent.left = newNode;
            } else {
                oldNode.parent.right = newNode;
            }
        }
        newNode.parent = oldNode.parent;
    }
}