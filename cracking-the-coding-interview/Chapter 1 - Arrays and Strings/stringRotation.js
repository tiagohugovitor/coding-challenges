const stringRotation = function (s, p) {
    const size = s.length
    if (size !== p.length) {
        return false
    }
    // s = xy, p = yx
    const yxyx = p + p
    if (yxyx.includes(s)) {
        return true
    }
    return false
}

console.log(stringRotation('waterbottle', 'erbottlewat'))