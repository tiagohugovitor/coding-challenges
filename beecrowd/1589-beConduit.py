# 1589-beConduit.py
# Problem: Be Conduit
# Link: https://judge.beecrowd.com/en/problems/view/1589
# Solved on: 2024-08-25

def beConduit():
    tests = int(input())
    for _ in range(tests):
        r1, r2 = map(int, input().split())
        result = (r1+r2)
        print(result)
beConduit()