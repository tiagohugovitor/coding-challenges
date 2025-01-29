const findDuplicate = function (nums) {
    const size = nums.length
    
    if (size === 1) return 1
    
    for(let i=0; i< size; i++) {
        const num = Math.abs(nums[i]) - 1
        if (nums[num] < 0) {
            return num + 1
        }
        nums[num] = - nums[num]
    }
}

console.log(findDuplicate([1,3,4,2,2]))
