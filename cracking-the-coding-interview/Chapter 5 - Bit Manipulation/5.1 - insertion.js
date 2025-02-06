const insertion = (n, m, i, j) => {
    const startMask = (1 << j + 1) - 1
    const endMask = (1 << i + 1) - 1
    const mask = ~(startMask - endMask)
    const nCleared = n & mask
    const mShifted = m << i
    return nCleared | mShifted
}

console.log(insertion(1024, 19, 2, 6))