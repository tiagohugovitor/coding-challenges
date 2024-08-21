# 1079-weightedAverages.py
# Problem: Weighted Averages
# Link: https://judge.beecrowd.com/en/problems/view/1079
# Solved on: 2024-08-20

def weightedAverages():
    n = int(input())
    
    for i in range(0, n):
        a, b, c = map(float, input().split())
        average = (a*2 + b*3 + c*5)/10
        print(f'{average:.1f}')

weightedAverages()