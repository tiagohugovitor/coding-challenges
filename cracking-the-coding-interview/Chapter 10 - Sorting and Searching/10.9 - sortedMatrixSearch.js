const sortedMatrixSearch = (matrix, target) => {
    const lines = matrix.length
    const columns = matrix[0].length - 1

    let row = 0
    let col = columns 

    while( row < lines && col >=0) {
        if(matrix[row][col] === target) {
            return [row, col]
        }
        if (matrix[row][col] > target) {
            col -= 1
        } else {
            row += 1
        }
    }

    return [-1,-1]
}

console.log(sortedMatrixSearch([[15,20,40,85], [20,35,80,95], [30, 55, 95, 105], [40, 80, 100, 120]], 55))