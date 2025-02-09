const groupAnagrams = (array) => {
    const mapAnagrams =  {}

    for (const word of array) {
        const orderedWord = word.split('').sort().join('')
        if (mapAnagrams[orderedWord]) {
            mapAnagrams[orderedWord] = [...mapAnagrams[orderedWord], word]
        }
        else {
            mapAnagrams[orderedWord] = [word]
        }
    }

    let index = 0

    for (const key in mapAnagrams) {
        const list = mapAnagrams[key]
        for (const word of list) {
            array[index] = word
            index += 1
        }
    }
    return array
}
const words = ["listen", "enlist", "rat", "tar", "art", "evil", "vile", "live", "silent", "banana"];
console.log(groupAnagrams(words))