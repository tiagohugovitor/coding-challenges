const searchInRotatedArray = (array, target) => {
    let start = 0
    let end = array.length - 1
    while (start <= end) {
        const middle = Math.floor((start + end)/2)
        if (array[middle] === target) {
            return middle
        }
        if (array[middle] <= array[end]) {
            if(target > array[middle] && target <= array[end]) {
                start = middle + 1
            } else {
                end = middle - 1
            }
        }
        else {
            if (target < array[middle] && target >= array[start]) {
                end = middle - 1
            } else {
                start = middle + 1
            }
        }
    }

    return -1
}

console.log(searchInRotatedArray([3,4,5,6,1,2], 2))