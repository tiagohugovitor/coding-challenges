# 3162-spaceCommunication.py
# Problem: Space Communication
# Link: https://judge.beecrowd.com/en/problems/view/3162
# Solved on: 2024-10-31

import math

def spaceCommunication():
    shipsAmount = int(input())
    shipsCoordinates = [0] * shipsAmount
    
    for ship in range(shipsAmount):
        shipsCoordinates[ship] = list(map(int, input().split()))

    for shipA in range(shipsAmount):
        minimumDistance = float('inf')
        for shipB in range(shipsAmount):
            if shipA == shipB:
                continue
            distanceShipAShipB = math.sqrt(pow(shipsCoordinates[shipA][0] - shipsCoordinates[shipB][0], 2) + pow(shipsCoordinates[shipA][1] - shipsCoordinates[shipB][1], 2) + pow(shipsCoordinates[shipA][2] - shipsCoordinates[shipB][2], 2))
            if distanceShipAShipB < minimumDistance:
                minimumDistance = distanceShipAShipB
            if minimumDistance <= 20:
                break
        if minimumDistance <= 20:
            print('A')
            continue
        if minimumDistance <= 50:
            print('M')
            continue
        print('B')        

spaceCommunication()
