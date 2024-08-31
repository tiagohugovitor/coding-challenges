# 2163-forceAwakens.py
# Problem: The Force Awakens
# Link: https://judge.beecrowd.com/en/problems/view/2163
# Solved on: 2024-08-30

def forceAwakens():

    def checkIfIsSaber(matrix, i, j):
        for line in [-1, 0, 1]:
            for column in [-1, 0, 1]:
                if line == 0 and column == 0:
                    continue
                if matrix[line + i][column + j] != 7:
                    return False

        return True
            
        
    lines, columns = map(int, input().split())
    matrix = [0] * lines
    for i in range(lines):
        matrix[i] = list(map(int, input().split()))

    for i in range(1, lines - 1):
        for j in range(1, columns - 1):
            if matrix[i][j] == 42 and checkIfIsSaber(matrix, i, j):
                print(f'{i + 1} {j + 1}')
                return
    print('0 0')

forceAwakens()
