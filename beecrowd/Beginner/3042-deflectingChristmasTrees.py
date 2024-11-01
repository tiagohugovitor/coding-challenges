# 3042-deflectingChristmasTrees.py
# Problem: Deflecting from Christmas Trees
# Link: https://judge.beecrowd.com/en/problems/view/3042
# Solved on: 2024-10-31
import sys

def deflectingChristmasTrees():
    data = sys.stdin.read().splitlines()
    idx = 0
    
    while True:
        distance = int(data[idx])
        idx += 1

        if distance == 0:
            break

        labirinth = [0] * distance
        minimumChanges = [0] * distance

        for i in range(distance):
            labirinth[i] = list(map(int, data[idx].split()))
            idx += 1

        minimumChanges[0] = [1, 0, 1]

        for lane in range(3):
            if labirinth[0][lane] == 1:
                minimumChanges[0][lane] = float('inf') 

        for path in range(1, distance):
            minimumChanges[path] = [0, 0, 0]
            for lane in range(3):
                if labirinth[path][lane] == 1:
                    minimumChanges[path][lane] = float('inf')
                    continue
                if lane == 0:
                    minimumChanges[path][0] = min(minimumChanges[path - 1][0], minimumChanges[path -1][1] + 1, minimumChanges[path - 1][2] + 2)
                if lane == 1:
                    minimumChanges[path][1] = min(minimumChanges[path - 1][1], minimumChanges[path - 1][0] + 1, minimumChanges[path - 1][2] + 1)
                if lane == 2:
                    minimumChanges[path][2] = min(minimumChanges[path - 1][2], minimumChanges[path - 1][0] + 2, minimumChanges[path - 1][1] + 1)

        print(min(minimumChanges[distance - 1][0], minimumChanges[distance - 1][1], minimumChanges[distance - 1][2]))

deflectingChristmasTrees()
