# 1180-lowestNumberAndPosition.py
# Problem: Lowest Number and Position
# Link: https://judge.beecrowd.com/en/problems/view/1180
# Solved on: 2024-08-22

def lowestNumberAndPosition():
    n = int(input())
    x = list(map(int, input().split()))
    minValue = x[0]
    position = 0
    for i in range(1, n):
        if x[i] < minValue:
            minValue = x[i]
            position = i

    print(f'Menor valor: {minValue}')
    print(f'Posicao: {position}') 

lowestNumberAndPosition()