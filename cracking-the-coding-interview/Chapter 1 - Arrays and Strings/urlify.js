// O(n)
const urlify = function (s) {
    const url = s.replace(/ /g, '%20')

    return url
}

console.log(urlify('teste teste teste'))