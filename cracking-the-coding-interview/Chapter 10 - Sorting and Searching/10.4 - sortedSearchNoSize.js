const sortedSearchNoSize = (array, target) => {
    if (array[0] === target) {
        return 0
    }
    let index = 1
    while (array[index] !== -1 && array[index] < target) {
        index *= 2
    }

    const length = index
    let start = length / 2
    let end = length
    
    while(start <= end) {
        const middle = Math.floor((start+end) /2)
        if (array[middle] === target) {
            return middle
        }
        if (array[middle] > target || array[middle] === -1) {
            end = middle - 1
        }
        else {
            start = middle + 1
        }
    }
    return -1 
}

const array = [1, 3, 5, 7, 9, 15, 20, 25, 30, 35, 40, -1, -1, -1, -1, -1, -1]

console.log(sortedSearchNoSize(array, 15));
console.log(sortedSearchNoSize(array, 30));
console.log(sortedSearchNoSize(array, 100));