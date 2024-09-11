# 2552-cheeseBreadSweeper.py
# Problem: CheeseBreadSweeper
# Link: https://judge.beecrowd.com/en/problems/view/2552
# Solved on: 2024-09-05

def cheeseBreadSweeper():
    while True:
        try:
            rows, columns = map(int, input().split())
            matrix = [0] * rows

            for row in range(rows):
                matrix[row] = list(map(int, input().split()))

            for i in range(rows):
                for j in range(columns):
                    if matrix[i][j] == 1:
                        print('9', end='')
                    else:
                        left = matrix[i][j-1] if j-1 >= 0 else 0 
                        right = matrix[i][j+1] if j+1 < columns else 0
                        top = matrix[i-1][j] if i-1 >= 0 else 0
                        bottom = matrix[i+1][j] if i+1 < rows else 0

                        total = left + right + bottom + top
                        print(total, end='')
                    
                print()

        except EOFError:
            break

cheeseBreadSweeper()
