# 3209-electricalOutlets.py
# Problem: Electrical Outlets
# Link: https://judge.beecrowd.com/en/problems/view/3209
# Solved on: 2024-10-23

def electricalOutlets():
    tests = int(input())

    for _ in range(tests):
        strips = list(map(int, input().split()))
        sumStrips = 0
        for i in range(1, strips[0] + 1):
            sumStrips += strips[i] - 1

        sumStrips += 1

        print(sumStrips)

electricalOutlets()
