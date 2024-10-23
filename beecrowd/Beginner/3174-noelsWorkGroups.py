# 3174-noelsWorkGroups.py
# Problem: Noel's Work Groups
# Link: https://judge.beecrowd.com/en/problems/view/3174
# Solved on: 2024-10-23

def noelsWorkGroups():
    duration = {
        'bonecos': 8,
        'arquitetos': 4,
        'musicos': 6,
        'desenhistas': 12,
    }

    capableWork = {
        'bonecos': 0,
        'arquitetos': 0,
        'musicos': 0,
        'desenhistas': 0,
    }

    elves = int(input())
    
    for _ in range(elves):
        _, classification, time = input().split()
        capableWork[classification] += int(time)

    totalGifts = 0

    for classification in capableWork:
        totalGifts += capableWork[classification] // duration[classification]

    print(totalGifts)

noelsWorkGroups()
