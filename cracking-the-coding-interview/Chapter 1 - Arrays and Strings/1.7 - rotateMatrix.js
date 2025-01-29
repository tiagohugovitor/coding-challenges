// O(n2)
const rotateMatrix = function (m) {
    const size = m.length
    let rotated = new Array(size)

    for (let i=0;i< size; i++) {
        rotated[i] = new Array(size)
    }

    for (let i=0; i<size; i++) {
        for (let j=0; j<size; j++) {
            rotated[i][j] = m[size - j - 1][i]
        }
    }
    return rotated
}

console.log(rotateMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))

const rotateMatrixInPlace = function (m) {
    const size = m.length;

    for (let layer = 0; layer < Math.floor(size / 2); layer++) {
        const first = layer;
        const last = size - layer - 1;

        for (let i = first; i < last; i++) {
            const offset = i - first;

            const top = m[first][i];

            // Left -> Top
            m[first][i] = m[last - offset][first];

            // Bottom -> Left
            m[last - offset][first] = m[last][last - offset];

            // Right -> Bottom
            m[last][last - offset] = m[i][last];

            // Top -> Right
            m[i][last] = top;
        }
    }

    return m;
};

console.log(rotateMatrixInPlace([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]));