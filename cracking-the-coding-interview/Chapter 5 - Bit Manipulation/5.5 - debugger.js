const debuggerCode = (number) => {
    return (number & (number - 1)) === 0
}

console.log(debuggerCode(8))

// The code checks if number is a power of 2.
// 1000 & 0111 = 0
