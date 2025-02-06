const pairwiseSwap = (number) => {
    return (((number & 0xaaaaaaaa) >>> 1) | ((number & 0x55555555) << 1))
}

console.log(pairwiseSwap(115))