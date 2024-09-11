# 2551-newRecord.py
# Problem: New Record
# Link: https://judge.beecrowd.com/en/problems/view/2551
# Solved on: 2024-09-05

def newRecord():
    while True:
        try:
            trainings = int(input())
            average = 0
            for day in range(trainings):
                time, distance = map(int, input().split())
                current = distance / time
                if current > average:
                    average = current
                    print(day + 1)

        except EOFError:
            break

newRecord()
