const binarySearchRecursive = (array, start, end, target) => {
    if (start > end) return null

    const middle = Math.floor((start + end) / 2)
    if (array[middle] === target) {
        return middle
    }
    if (array[middle] > target) {
        return binarySearchRecursive(array, start, middle - 1, target)
    }
    else {
        return binarySearchRecursive(array, middle + 1, target)
    }
}

const binarySearchIterative = (array, target) => {
    if (array.size === 0) return null
    let start = 0
    let end = array.length - 1

    while(start <= end) {
        const middle = Math.floor((start + end) / 2)
        if (array[middle] === target){
            return middle
        }
        if (array[middle] > target){
            end = middle - 1
        }
        if (array[middle] < target){
            start = middle + 1
        }
    }

    return null
}

console.log(binarySearchRecursive([1,2,3,4,5,6,7,8,9], 0, 8, 2))
console.log(binarySearchIterative([1,2,3,4,5,6,7,8,9], 2))