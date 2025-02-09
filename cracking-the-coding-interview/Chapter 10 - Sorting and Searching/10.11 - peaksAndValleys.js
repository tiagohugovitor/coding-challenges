const peaksAndValleys = (array) => {
    if (array.length < 2) return array

    for (let i=1; i < array.length; i+=2) {
        const biggestIndex = maxIndex(array, i-1, i, i+1)
        if( i !== biggestIndex) {
            swap(array, i, biggestIndex)
        }
    }

    return array
}

const maxIndex = (array, a, b, c) => {
    const size = array.length

    const aValue = a >= 0 && a < size ? array[a] : Number.MIN_VALUE
    const bValue = b >= 0 && b < size ? array[b] : Number.MIN_VALUE
    const cValue = c >= 0 && c < size ? array[c] : Number.MIN_VALUE

    const max = Math.max(aValue, bValue, cValue)

    if (max === aValue) return a
    if (max === cValue) return c
    return b
}

const swap = (array, first, second) => {
    const temp = array[first]
    array[first] = array[second]
    array[second] = temp
}

console.log(peaksAndValleys([5,3,1,2,3]))