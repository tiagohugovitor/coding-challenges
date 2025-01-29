const minimumWindowSubstring = function (s, t) {
    const substring = new Set()
    const window = new Set()
    let minimumWindow = [0,0]

    let leftPointer = 0
    let rightPointer = 0

    for (const char of t) {
        if(substring.has(char)) {
            substring[char] += 1
        }
        else {
            substring.add(char)
            substring[char] = 1
        }
        window.add(char)
        window[char] = 0
    }

    let hasRightPointerMoved = true

    while(rightPointer < s.length) {
        if (hasRightPointerMoved) {
            const currentChar = s[rightPointer]
    
            if (substring.has(currentChar)) {
                window[currentChar] += 1
            }
        }

        let isSubstring = true

        for (const char of window) {
            if (window[char] < substring[char] ) {
                isSubstring = false
                break
            }
        }

        if (isSubstring) {
            if (minimumWindow[1] == 0 || ((minimumWindow[1] - minimumWindow[0]) > rightPointer - leftPointer)) {
                minimumWindow = [leftPointer, rightPointer + 1]
            }

            if (substring.has(s[leftPointer])) {
                window[s[leftPointer]] -= 1
            }

            leftPointer += 1
            hasRightPointerMoved = false
        }

        else {
            rightPointer += 1
            hasRightPointerMoved = true
        }
    }

    return s.slice(minimumWindow[0], minimumWindow[1])

}

console.log(minimumWindowSubstring('a', 'a'))