const addNeighboor = function (neighboors, line, column) {
    const startLine = Math.max(0, line - 1)
    const endLine = Math.min(neighboors.length - 1, line + 1)
    const startColumn = Math.max(0, column - 1)
    const endColumn = Math.min(neighboors[0].length - 1, column + 1)
    
    for (let i=startLine; i <= endLine; i++) {
        for (let j=startColumn; j <= endColumn; j++) {
            if(i !== line || j !== column) {
                neighboors[i][j] += 1
            }
        }
    }
}

const gameOfLife = function (board) {
    const lines = board.length
    const columns = board[0].length

    let neighboors = new Array(lines).fill(0)

    for (let i=0;i<lines;i++) {
        neighboors[i] = new Array(columns).fill(0)
    }

    for (let i=0;i<lines;i++) {
        for (let j =0;j<columns;j++) {
            if (board[i][j] == 1) {
                addNeighboor(neighboors, i, j)
            }
        }
    }

    for (let i =0;i<lines;i++) {
        for (let j =0;j<columns;j++) {
            let newState = 0;
            if (board[i][j] === 0 && neighboors[i][j] === 3) {
                newState = 1
            }
            else if (board[i][j] === 1 && (neighboors[i][j] === 3 || neighboors[i][j] === 2)) {
                newState = 1
            } 
            board[i][j] = newState
        }
    }
}

console.log(gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))