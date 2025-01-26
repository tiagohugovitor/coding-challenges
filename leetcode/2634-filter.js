/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const result = []
    for (let i=0; i < arr.length; i++) {
        const filtered = fn(arr[i], i)
        if (filtered)
            result.push(arr[i])
    }

    return result
};