// O(s log s + p log p)
const checkPermutationOrdering = function (s, p) {
    const orderedS = s.split('').sort().join('')
    const orderedP = p.split('').sort().join('')

    if (orderedP === orderedS) {
        return true
    }

    return false
}

console.log(checkPermutationOrdering('teste', 'setteg'));

// 0(s + p)

const checkPermutation = function (s, p) {
    if (s.length !== p.length) {
        return false
    }

    const frequency = {}

    for (const char of s) {
        frequency[char] = (frequency[char] || 0) + 1;
    }

    for (const char of p) {
        if (!frequency[char]) return false;
        frequency[char]--;
    }

    return true;
}

console.log(checkPermutation('teste', 'ttttt'));