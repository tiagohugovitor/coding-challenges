# 2057-timeZone.py
# Problem: Time Zone
# Link: https://judge.beecrowd.com/en/problems/view/2057
# Solved on: 2024-08-28

def timeZone():
    departure, duration, zone = map(int, input().split())
    arrivalTime = departure + duration + zone
    if arrivalTime < 0:
        arrivalTime += 24
    elif arrivalTime >= 24:
        arrivalTime -= 24

    print(arrivalTime)

timeZone()
