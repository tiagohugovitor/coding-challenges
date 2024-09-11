# 2167-engineFailure.py
# Problem: Engine Failure
# Link: https://judge.beecrowd.com/en/problems/view/2167
# Solved on: 2024-08-31

def engineFailure():
    number = int(input())
    measures = list(map(int, input().split()))
    failure = 0

    for i in range(1, number):
        if measures[i] < measures[i-1]:
            failure = i + 1
            break

    print(failure)

engineFailure()
