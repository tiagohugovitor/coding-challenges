# 2520-analogimon.py
# Problem: The Last Analogimon
# Link: https://judge.beecrowd.com/en/problems/view/2520
# Solved on: 2024-09-04

def analogimon():
    while True:
        try:
            rows, columns = map(int, input().split())
            field = [0] * rows
            for i in range(rows):
                field[i] = list(map(int, input().split()))
            analogimonCoordinates = ()
            playerCoordinates = ()
            for i in range(rows):
                for j in range(columns):
                    if field[i][j] == 2:
                        analogimonCoordinates = (i, j)
                    if field[i][j] == 1:
                        playerCoordinates = (i, j)
            
            time = abs(analogimonCoordinates[0] - playerCoordinates[0]) + abs(analogimonCoordinates[1] - playerCoordinates[1])
            print(time)
        
        except EOFError:
            break

analogimon()
