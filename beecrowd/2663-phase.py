# 2663-phase.py
# Problem: Phase
# Link: https://judge.beecrowd.com/en/problems/view/2663
# Solved on: 2024-09-06

def phase():
    contestants = int(input())
    minimumSpots = int(input())
    scores = [0] * contestants
    for person in range(contestants):
        scores[person] = int(input())
    
    scores.sort(reverse=True)
    classifieds = minimumSpots
    i = minimumSpots

    while i < len(scores) and scores[i-1] == scores[i]:
        classifieds += 1
        i += 1

    print(classifieds)



phase()
