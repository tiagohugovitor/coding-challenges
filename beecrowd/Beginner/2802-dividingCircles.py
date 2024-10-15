# 2802-dividingCircles.py
# Problem: Dividing Circles
# Link: https://judge.beecrowd.com/en/problems/view/2802
# Solved on: 2024-10-15

def dividingCircles():
    n = int(input())
    divisions =  1 + (((n-1)*n)/2) + (((n) * (n - 1) * (n - 2 ) * (n - 3))/24)
    print(int(divisions))


dividingCircles()
