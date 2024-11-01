# 2785-pyramid.py
# Problem: Pyramid
# Link: https://judge.beecrowd.com/en/problems/view/2785
# Solved on: 2024-10-14

#NOT WORKING AS EXPECTED

def pyramid():
    size = int(input())
    boxes = [0] * size
    weights = [0] * size
    
    for i in range(size):
        boxes[i] = list(map(int, input().split()))
        weights[i] = [0] * size

    weights[size - 1] = boxes[size - 1]

    for line in range(size - 2, -1, -1):
        for start in range(size - line):
            weights[line][start] = sum(boxes[line][start:start + line + 1])
            for offset in range(line + 1):
                weights[line][start] = min(weights[line][start], weights[line + 1][start + offset] + sum(boxes[line][start:start + line + 1]))

    pyramidWeight = min(weights[0][:size])
    print(pyramidWeight)

pyramid()
