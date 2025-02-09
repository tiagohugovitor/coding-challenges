

const sparseSearch = (words, target) => {
    let start = 0
    let end = words.length - 1

    while (start <= end) {
        let middle = Math.floor((start+end)/2)
        if (array[middle] === '') {
            let left = middle - 1
            let right = middle + 1
            while (true) {
                if (left < start && right > end) {
                    return -1
                }
                if (right <= end && words[right] !== '') {
                    middle = right
                    break
                }
                if (left >= start && words[left] !== '') {
                    middle = left
                    break
                }
                left -= 1
                right += 1
            }
        }
        if (array[middle] === target) {
            return middle
        }
        if (array[middle] > target) {
            end = middle - 1
        }
        else {
            start = middle + 1
        }
    }
    return -1 
}

const array = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
console.log(sparseSearch(array, "ball"))
