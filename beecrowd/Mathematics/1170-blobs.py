# 1170-blobs.py
# Problem: Blobs
# Link: https://judge.beecrowd.com/en/problems/view/1170
# Solved on: 2024-11-18

import sys

def blobs():
    input_data = sys.stdin.read().splitlines()
    i = 1

    for _ in range(int(input_data[0])):
        food = float(input_data[i])
        i += 1
        days = 0

        while food > 1.0:
            food /= 2
            days += 1
        
        print(f'{days} dias')
        
blobs()
