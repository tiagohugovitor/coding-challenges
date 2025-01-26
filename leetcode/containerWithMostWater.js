const containerWithMostWater = function (height) {
    let maxWater = 0
    let leftPointer = 0
    let rightPointer = height.length - 1

    while (leftPointer < rightPointer) {
        const amountOfWater = Math.min(height[leftPointer], height[rightPointer]) * (rightPointer - leftPointer)
        if (amountOfWater > maxWater) {
            maxWater = amountOfWater
        }
        if (height[leftPointer] > height[rightPointer]) {
            rightPointer -= 1
        }
        else {
            leftPointer += 1
        }
    }
    return maxWater
}

console.log(containerWithMostWater([1,8,6,2,5,4,8,3,7]))