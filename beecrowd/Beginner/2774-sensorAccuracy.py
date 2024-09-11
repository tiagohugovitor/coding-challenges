# 2774-sensorAccuracy.py
# Problem: Sensor Accuracy
# Link: https://judge.beecrowd.com/en/problems/view/2774
# Solved on: 2024-09-11

import sys
import math

def sensorAccuracy():
    input = sys.stdin.read
    data = input().splitlines()
    i = 0
    while i < len(data):
        h, m = map(int, data[i].split())
        i += 1
        x = list(map(float, data[i].split()))
        i += 1
        average = sum(x)/ len(x)
        total = 0
        for j in range(len(x)):
            total += pow((x[j] - average), 2)
        
        accuracy = math.sqrt(total / (len(x) - 1))

        print(f'{accuracy:.5f}')

sensorAccuracy()
