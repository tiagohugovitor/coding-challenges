// O(s log s)
const palindromePermutationOrdering = function (s) {
    const stringLowerWithoutSpaces = s.replace(/ /g, '').toLowerCase()
    const size = stringLowerWithoutSpaces.length
    const isSizeOdd = size % 2 !== 0
    const orderedString = stringLowerWithoutSpaces.split('').sort().join('')

    let singleChar = 0
    let i = 0
    while (i < size && singleChar < 2) {
        if ( i + 1 == size) {
            singleChar += 1
            break
        }

        if ( orderedString[i] == orderedString[i+1]) {
            i = i + 2
        }
        else {
            singleChar += 1
            i += 1
        }
    }

    if ((isSizeOdd && singleChar === 1) || (!isSizeOdd && singleChar == 0)) {
        return true
    }

    return false
}

//console.log(palindromePermutationOrdering('Tact coa'))

// 0(s)
const palindromePermutation = function (s) {
    const stringLowerWithoutSpaces = s.replace(/ /g, '').toLowerCase();

    const frequency = {}

    for (const char of stringLowerWithoutSpaces) {
        frequency[char] = (frequency[char] || 0) + 1
    }

    let oddFrequency = 0

    for (const char in frequency) {
        if (frequency[char] % 2 !== 0) {
            oddFrequency += 1
        }
        if (oddFrequency > 1) {
            return false
        }
    }

    return true
}

console.log(palindromePermutation('Tact coa'))