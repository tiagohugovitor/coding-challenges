const longestConsecutiveNumbersOrdering = function (nums) {
    const size = nums.length

    if (size < 2) {
        return size
    }

    const sortedNumbers = nums.sort((a,b) => a - b)
    let current = sortedNumbers[0] 
    let count = 1
    let maxCount = 1
    
    for (let i = 1; i< size; i++) {
        if (current === sortedNumbers[i]) {
            continue
        }
        if (current + 1 === sortedNumbers[i]) {
            current += 1
            count += 1
            continue
        }
        if (count > maxCount) {
            maxCount = count
        }
        count = 1
        current = sortedNumbers[i]
    }

    return maxCount
}

console.log(longestConsecutiveNumbersOrdering([100,4,200,1,3,2]))

const longestConsecutiveNumbers = function (nums) {
    if (nums.length === 0) {
        return 0
    }

    const numSet = new Set(nums)
    let maxLength = 0

    for (const num of numSet) {
        if (!numSet.has(num - 1)) {
            let count = 1
            let currentNumber = num
            while(numSet.has(currentNumber + 1)) {
                currentNumber += 1
                count += 1
            }
            if (count > maxLength) {
                maxLength = count
            } 
        }
    }

    return maxLength
}

console.log(longestConsecutiveNumbers([-8,-2,-3,-9,-6,7,9,-8,9,2,-8]))
