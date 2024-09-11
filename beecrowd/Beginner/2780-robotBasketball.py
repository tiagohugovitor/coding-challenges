# 2780-robotBasketball.py
# Problem: Robot Basketball
# Link: https://judge.beecrowd.com/en/problems/view/2780
# Solved on: 2024-09-11

def robotBasketball():
    points = {
        800: 1,
        1400: 2,
        2000: 3,
    }
    distance = int(input())
    for line in points:
        if distance <= line:
            print(points[line])
            break


robotBasketball()
