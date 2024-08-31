# 2162-peaksAndValleys.py
# Problem: Peaks and Valleys
# Link: https://judge.beecrowd.com/en/problems/view/2162
# Solved on: 2024-08-30

def peaksAndValleys():
    width = int(input())
    measures = list(map(int, input().split()))

    peak = 0 if measures[1] > measures[0] else 1
    hasPattern = 1
    for i in range(0, width - 1):
        if (measures[i] == measures[i+1]) or (peak and measures[i+ 1] > measures[i]) or (not peak and measures[i+1] < measures[i]):
            hasPattern = 0
            break
        peak = 0 if peak == 1 else 1
    
    print(f'{hasPattern}')

peaksAndValleys()
