# 3343-attackOnGasparini.py
# Problem: Attack on Gasparini
# Link: https://judge.beecrowd.com/en/problems/view/3343
# Solved on: 2024-09-03

# Still not working - time limit exceed

def attackOnGasparini():
    _, wallsSize = map(int,input().split())
    titansSequence = input()
    p, m, g = map(int, input().split())
    titansSizes = {
        'P': p,
        'M': m,
        'G': g
    }
    walls = [wallsSize]
    pointerStandingWall = 0

    for titan in titansSequence:
        defated = False
        start = len(walls) - 1 if titan == 'G' else pointerStandingWall
        for wall in range(start, len(walls)):
            if titansSizes[titan] <= walls[wall]:
                walls[wall] -= titansSizes[titan]
                if walls[wall] == 0 or walls[wall] < titansSizes['P']:
                    pointerStandingWall += 1
                defated = True
                break
        if not defated:
            walls.append(wallsSize - titansSizes[titan])

    print(len(walls))

attackOnGasparini()
