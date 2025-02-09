const sortedMerge = (firstArray, secondArray) => {
    const totalSize = firstArray.length - 1
    let secondPointer = secondArray.length - 1
    let firstPointer = totalSize - secondPointer - 1
    let current = totalSize

    while (firstPointer >= 0 && secondPointer >= 0) {
        if(firstArray[firstPointer] > secondArray[secondPointer]) {
            firstArray[current] = firstArray[firstPointer]
            firstPointer -= 1
        }
        else {
            firstArray[current] = secondArray[secondPointer]
            secondPointer -= 1
        }
        current -= 1
    }

    while (secondPointer >= 0) {
        firstArray[current] = secondArray[secondPointer]
        secondPointer -= 1
        current -= 1
    }

    return firstArray
}

const firstArray = [1,2,3,4,5,6,7,8,9,10, null, null, null, null, null]
const secondArray = [1,2,3,4,5]

console.log(sortedMerge(firstArray, secondArray))