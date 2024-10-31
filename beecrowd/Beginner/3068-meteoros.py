# 3068-meteoros.py
# Problem: Meteoros
# Link: https://judge.beecrowd.com/en/problems/view/3068
# Solved on: 2024-10-30

def meteoros():
    tests = 0
    while True:
        tests += 1
        farm = list(map(int, input().split()))
        if farm[0] == 0 and farm[1] == 0 and farm[2] == 0 and farm[3] == 0:
            break
        meteorosAmount = int(input())
        meteorosInsideFarm = 0
        for _ in range(meteorosAmount):
            coordenates = list(map(int, input().split()))
            if coordenates[0] >= farm[0] and coordenates[0] <= farm[2] and coordenates[1] >= farm[3] and coordenates[1] <= farm[1]:
                meteorosInsideFarm += 1

        print(f'Teste {tests}')
        print(meteorosInsideFarm)

meteoros()
