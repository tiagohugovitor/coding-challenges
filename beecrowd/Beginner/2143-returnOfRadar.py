# 2143-returnOfRadar.py
# Problem: The Return of Radar
# Link: https://judge.beecrowd.com/en/problems/view/2143
# Solved on: 2024-08-29

def returnOfRadar():
    while True:
        tests = int(input())
        if tests == 0:
            break
        for _ in range(tests):
            people = int(input())
            corner = 2 if people % 2 == 0 else 1
            total = (people - corner) * 2 + corner

            print(total)

returnOfRadar()
