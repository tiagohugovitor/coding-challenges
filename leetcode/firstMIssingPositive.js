const firstMissingPositiveOrdering = function (nums) {
    orderedNums = nums.sort((a,b) => a - b)
    let i = 0
    let searched = 1
    
    while ( i < orderedNums.length && orderedNums[i] <= searched) {
        if (searched == orderedNums[i]) {
            searched += 1
        }
        i += 1
    }
    
    return searched
}

console.log(firstMissingPositiveOrdering([3,4,-1,1]))

const firstMissingPositiveLinear = function (nums) {
    const size = nums.length
    let containsOne = false
    for (let index=0; index < size; index++) {
        if (nums[index] === 1) {
            containsOne = true
        }
        if (nums[index] < 1 || nums[index] > size) {
            nums[index] = 1
        }
    }

    if (!containsOne) {
        return 1
    }

    for (let index= 0; index < size; index++)  {
        const absIndex = Math.abs(nums[index]) - 1
        nums[absIndex] =  nums[absIndex] < 0 ? nums[absIndex] : - nums[absIndex]
    }

    for (let index= 0; index < size; index++)  {
        if(nums[index] > 0) {
            return index + 1
        }
    }

    return size + 1
}

console.log(firstMissingPositiveLinear([1]))
