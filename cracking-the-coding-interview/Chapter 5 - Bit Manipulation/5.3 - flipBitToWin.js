const flipBitToWin = (number) => {
    let flippedCount = 0
    let currentCount = 0

    let maxLength = 0

    while ( number !== 0) {
        if ((number & 1) === 1) { //current bit is 1
            flippedCount += 1
            currentCount += 1
        } else if ((number & 1) === 0) { //current bit is 0
            if (flippedCount > maxLength) {
                maxLength = flippedCount
            }
            flippedCount = currentCount + 1
            currentCount = 0
        }
        number >>>= 1
    }
    return maxLength
}

console.log(flipBitToWin(1775))