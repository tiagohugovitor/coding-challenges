// get a value of a bit in position i
// returns false for 0 and true for 1
export const getBit = (number, position) => {
    const mask = 1 << position
    return number & mask !== 0
}

// set a bit in position i to 1
export const setBit = (number, position) => {
    const mask = 1 << position
    return number | mask
}

// set a bit in position i to 0
export const clearBit = (number, position) => {
    const mask = ~( 1 << position)
    return number & mask
}

// set all most significant bits than position i (included) to 0
export const clearAllMSB = (number, position) => {
    const mask = (1 << position) - 1
    return mask & number
}

// set all less significant bits than position i (included) to 0
export const clearAllLSB = (number, position) => {
    const mask = ~((1 << position + 1) - 1)
    return mask & number
}

// change value of a bit in position i
export const updateBit = (number, position, value) => {
    const clearedBitPosition = clearBit(number, position)
    const mask = value << position
    return mask | clearedBitPosition
}
