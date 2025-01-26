const spiralOrder = function (matrix) {
    const answer = []
    const lines = matrix.length
    const columns = matrix[0].length

    let firstLine = 0
    let firstColumn = 0
    let lastLine = lines - 1
    let lastColumn = columns - 1

    while (answer.length < lines * columns) {
        for (let i = firstColumn; i <= lastColumn; i++) {
            answer.push(matrix[firstLine][i])
        }
        firstLine += 1;
        if (answer.length === lines * columns) {
            break;
        }
        for (let i = firstLine; i <= lastLine; i++) {
            answer.push(matrix[i][lastColumn])
        }
        lastColumn -= 1;
        if (answer.length === lines * columns) {
            break;
        }
        for (let i = lastColumn; i >= firstColumn; i--) {
            answer.push(matrix[lastLine][i])
        }
        lastLine -= 1;
        if (answer.length === lines * columns) {
            break;
        }
        for (let i = lastLine; i >= firstLine; i--) {
            answer.push(matrix[i][firstColumn])
        }
        firstColumn += 1;
        if (answer.length === lines * columns) {
            break;
        }
    }    

    return answer
}

spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]);