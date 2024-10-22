# 3037-dartsByDistance.py
# Problem: Playing Darts by Distance
# Link: https://judge.beecrowd.com/en/problems/view/3037
# Solved on: 2024-10-21

def dartsByDistance():
    tests = int(input())

    for _ in  range(tests):
        maria = 0
        joao = 0

        for _ in range(3):
            distance, score = map(int, input().split())
            joao += distance * score

        for _ in range(3):
            distance, score = map(int, input().split())
            maria += distance * score

        if maria > joao:
            print('MARIA')
        else:
            print('JOAO')

dartsByDistance()
