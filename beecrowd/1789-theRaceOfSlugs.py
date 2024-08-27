# 1789-raceOfSlugs.py
# Problem: The Race of Slugs
# Link: https://judge.beecrowd.com/en/problems/view/1789
# Solved on: 2024-08-25

def raceOfSlugs():
    while True:
        try:
            amount = int(input())
            speeds = input().split()
            maxSpeed = 0
            for i in range(amount):
                if int(speeds[i]) >= 20:
                    maxSpeed = int(speeds[i])
                    break
                if int(speeds[i]) > maxSpeed:
                    maxSpeed = int(speeds[i])
            if maxSpeed < 10:
                print(1)
            elif maxSpeed < 20:
                print(2)
            else:
                print(3)
        except EOFError:
            break

raceOfSlugs()