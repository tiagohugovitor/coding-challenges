// O(n)
const oneAway = function (s, p) {
    if (s === p) {
        return true
    }

    if (Math.abs(s.length - p.length) > 1) {
        return false
    }

    let edits = 0
    let sPointer = 0, pPointer = 0

    while ( edits < 2 && sPointer < s.length && pPointer < p.length) {
        if (s[sPointer] === p[pPointer]) {
            sPointer += 1
            pPointer += 1
            continue
        }
        edits += 1
        if (s.length === p.length) {
            sPointer += 1
            pPointer += 1
            continue
        }
        if (s.length > p.length) {
            sPointer += 1
            continue
        }
        if (s.length < p.length) {
            pPointer += 1
            continue
        }
    }

    if (sPointer !== s.length || pPointer !== p.length) {
        edits += 1
    }

    return edits < 2
}

console.log(oneAway('pale', 'bake'))