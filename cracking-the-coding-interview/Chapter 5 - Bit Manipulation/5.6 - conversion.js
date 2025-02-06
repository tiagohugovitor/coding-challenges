const conversion = (numberA, numberB) => {
    let difference = numberA ^ numberB
    let count = 0
    while (difference != 0) {
        count += 1
        difference = (difference & (difference - 1))
    }

    return count
}

console.log(conversion(29, 15))