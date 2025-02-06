const binaryToString = (number) => {
    if (number <= 0 || number >= 1) return "Error"

    const binary = ['.']

    while (number > 0) {
        if (binary.length >= 32) {
            return "Error"
        }

        const r = number * 2
        
        if (r >= 1) {
            binary.push('1')
            number = r - 1
        }
        else {
            binary.push('0')
            number = r
        }
    }

    return binary.join('')
}

console.log(binaryToString(0.5))