# 2311-diving.py
# Problem: Diving
# Link: https://judge.beecrowd.com/en/problems/view/2311
# Solved on: 2024-09-04

def diving():
    divers = int(input())
    for _ in range(divers):
        name = input()
        difficulty = float(input())
        scores = list(map(float, input().split()))
        maxScore, minScore =  scores[0], scores[0]
        sum = 0
        for score in scores:
            sum += score
            if score < minScore:
                minScore = score
            elif score > maxScore:
                maxScore = score
        
        result = (sum - maxScore - minScore) * difficulty

        print(f'{name} {result:.2f}')

diving()
