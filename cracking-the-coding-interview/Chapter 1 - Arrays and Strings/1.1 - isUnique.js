// Should I remove spaces before starting the algorithm ?
// O(n log n)
const isUniqueOrdering = function (s) {
    const size = s.length
    const orderedS = s.split('').sort().join('')
    for (let i=0; i< size; i++) {
        const currentChar = orderedS[i]
        const nextChar = orderedS[i+1]
        if (currentChar === nextChar) {
            return false;
        }
    }
    return true;
}

console.log(isUniqueOrdering('tes'))

// O(n)
const isUnique = function(s) {
    const seen = new Set()

    for (let i=0; i< s.length; i++) {
        const character = s[i]
        if (seen.has(character)) {
            return false
        }
        seen.add(character)
    }

    return true
}

console.log(isUnique('tes e'))