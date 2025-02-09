const bubbleSort = (array) => {
    const size = array.length
    for (let i=size; i >= 0; i--) {
        let changed = false
        for (let j=0; j < i - 1; j ++) {
            if (array[j] > array[j+1]) {
                changed = true
                const temp = array[j+1]
                array[j+ 1] = array[j]
                array[j] = temp
            }
        }
        if (!changed) {
            break
        }
    }

    return array
}

const selectionSort = (array) => {
    const size = array.length
    for (let i = 1; i < size; i++) {
        let j = i - 1
        const current = array[i]
        while (j >= 0 && current < array[j]) {
            array[j+1] = array[j]
            j -=1
        }
        array[j+1] = current
    }
    return array
}

const merge = (array, start, middle, end) => {
    let leftArray = []
    let rightArray = []

    for (let i = start; i < middle + 1; i++) {
        leftArray.push(array[i])
    }

    for (let i = middle + 1; i < end + 1; i++) {
        rightArray.push(array[i])
    }

    let leftPointer = 0
    let rightPointer = 0

    while (leftPointer < leftArray.length && rightPointer < rightArray.length) {
        if (leftArray[leftPointer] <= rightArray[rightPointer]) {
            array[start + leftPointer + rightPointer] = leftArray[leftPointer]
            leftPointer ++
        } else {
            array[start + leftPointer + rightPointer] = rightArray[rightPointer]
            rightPointer ++
        }
    }

    while (leftPointer < leftArray.length) {
        array[start + leftPointer + rightPointer] = leftArray[leftPointer]
        leftPointer ++
    }
    
    while (rightPointer < rightArray.length) {
        array[start + leftPointer + rightPointer] = rightArray[rightPointer]
        rightPointer ++
    }
}

const mergeSort = (array, start, end) => {
    if (start < end) {
        const middle = Math.floor((start + end) / 2)
        mergeSort(array, start, middle)
        mergeSort(array, middle + 1, end)
        merge(array, start, middle, end)
    }
    return array
}

const partition = (array, start, end) => {
    const pivotIndex = Math.floor(Math.random() * (end - start + 1)) + start;
    const pivot = array[pivotIndex]
    array[pivotIndex] = array[start]
    array[start] = pivot
    let left = start + 1
    let right = start + 1

    while(right < end + 1) {
        if(array[right] < pivot) {
            const temp = array[left]
            array[left] = array[right]
            array[right] = temp
            left ++
        }
        right ++
    }

    array[start] = array[left - 1]
    array[left - 1] = pivot


    return left - 1
}

const quickSort = (array, start, end) => {
    if (start < end) {
        const pivotIndex = partition(array, start, end)
        quickSort(array, start, pivotIndex - 1)
        quickSort(array, pivotIndex + 1, end)
    }
    return array
}

const countingSort = (array, exp) => {
    let output = new Array(array.length).fill(0);
    let count = new Array(10).fill(0);

    for (let i = 0; i < array.length; i++) {
        let digit = Math.floor(array[i] / exp) % 10;
        count[digit]++;
    }

    for (let i = 1; i < 10; i++) {
        count[i] += count[i - 1];
    }

    for (let i = array.length - 1; i >= 0; i--) {
        let digit = Math.floor(array[i] / exp) % 10;
        output[count[digit] - 1] = array[i];
        count[digit]--;
    }

    for (let i = 0; i < array.length; i++) {
        array[i] = output[i];
    }
}

function radixSort(array) {
    const maxNum = Math.max(...array);

    for (let exp = 1; Math.floor(maxNum / exp) > 0; exp *= 10) {
        countingSort(array, exp);
    }

    return array;
}

function bucketSort(array, bucketSize = 5) {
    if (array.length === 0) return array;

    const minVal = Math.min(...array);
    const maxVal = Math.max(...array);

    const bucketCount = Math.floor((maxVal - minVal) / bucketSize) + 1;
    let buckets = Array.from({ length: bucketCount }, () => []);

    for (const num of array) {
        const index = Math.floor((num - minVal) / bucketSize);
        buckets[index].push(num);
    }

    return buckets.reduce((acc, bucket) => acc.concat(selectionSort(bucket)), []);
}


// console.log(bubbleSort([5,3,4,6,1,2]))
// console.log(bubbleSort([1,2,3,4,5,6]))

// console.log(selectionSort([5,3,4,6,1,2]))
// console.log(selectionSort([1,2,3,4,5,6]))

// console.log(mergeSort([5,3,4,6,1,2], 0, 5))
// console.log(mergeSort([1,2,3,4,5,6], 0, 5))

// console.log(quickSort([5,3,4,6,1,2], 0, 5))
// console.log(quickSort([1,2,3,4,5,6], 0, 5))

// console.log(countingSort([5,3,4,6,1,2], 1))
// console.log(countingSort([1,2,3,4,5,6], 1))

// console.log(radixSort([5,3,4,6,1,2]))
// console.log(radixSort([1,2,3,4,5,6]))

console.log(bucketSort([5,3,4,6,1,2]))
console.log(bucketSort([1,2,3,4,5,6]))