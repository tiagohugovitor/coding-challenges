
const fillWithZero = function(matrix, line, column) {
    for (let i=0; i<matrix.length; i++) {
        matrix[i][column] = 0
    }
    for (let j=0; j< matrix[0].length; j++) {
        matrix[line][j] = 0
    }
}

const zeroMatrix = function (m) {
    const lines = m.length
    if (lines === 0) {
        return m
    }
    const columns = m[0].length
    if (columns === 0) {
        return m
    }

    let newMatrix = new Array(lines)

    for (let i=0; i<lines;i++) {
        newMatrix[i] = new Array(columns).fill(null)
    }

    for (let i=0; i<lines; i++){
        for (let j=0; j<columns; j++) {
            if (m[i][j] === 0) {
                fillWithZero(newMatrix, i, j)
                break
            }
            else {
                if (newMatrix[i][j] === null) {
                    newMatrix[i][j] = m[i][j]
                }
            }
        }
    }

    return newMatrix
}

console.log(zeroMatrix([
    [ 13, 0, 5, 1 ],
    [ 14, 10, 6, 2 ],
    [ 15, 11, 7, 3 ],
    [ 16, 12, 0, 4 ]
  ]))