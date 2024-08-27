# 1858-theonsAnswer.py
# Problem: Theon's Answer
# Link: https://judge.beecrowd.com/en/problems/view/1858
# Solved on: 2024-08-26

def theonsAnswer():
    n = int(input())
    hits = list(map(int, input().split()))
    minValue = hits[0]
    minN = 0
    for i, hit in enumerate(hits):
        if hit < minValue:
            minValue = hit
            minN = i
    print(minN + 1)


theonsAnswer()
