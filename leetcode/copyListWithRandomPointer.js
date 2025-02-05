/**
 * // Definition for a _Node.
 * function _Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {_Node} head
 * @return {_Node}
 */
var copyRandomList = function(head) {
    const nodesRef = new Map()

    const copiedList = new Node(0, null)

    let originalCurrent = head
    let copiedCurrent = copiedList

    while (originalCurrent !== null) {
        const newNode = new Node(originalCurrent.val)
        copiedCurrent.next = newNode
        nodesRef.set(originalCurrent, newNode)
        copiedCurrent = copiedCurrent.next
        originalCurrent = originalCurrent.next
    }

    originalCurrent = head
    copiedCurrent = copiedList.next

    while (originalCurrent !== null) {
        if (originalCurrent.random === null) {
            copiedCurrent.random = null
        } else {
            copiedCurrent.random = nodesRef.get(originalCurrent.random)
        }
        originalCurrent = originalCurrent.next
        copiedCurrent = copiedCurrent.next
    }

    return copiedList.next
};