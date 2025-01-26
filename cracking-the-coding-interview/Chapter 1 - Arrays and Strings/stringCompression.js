// O(n)

const stringCompression = function (s) {
    const size = s.length
    
    if (size < 3) {
        return s
    }

    let count = 0
    let currentChar = s[0]
    let newString = ''

    for (let i=0; i<size; i++) {
        if (s[i] === currentChar) {
            count += 1
        }
        else {
            newString += `${currentChar}${count}`
            count = 1
            currentChar = s[i]
        }
    }

    newString += `${currentChar}${count}`

    if (newString.length >= size) {
        return s
    }
    return newString
}

console.log(stringCompression('aabccccaaa'))
