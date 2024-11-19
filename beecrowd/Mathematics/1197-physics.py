# 1197-physics.py
# Problem: Back to High School Physics
# Link: https://judge.beecrowd.com/en/problems/view/1197
# Solved on: 2024-11-18

import sys

def physics():
    input_data = sys.stdin.read().splitlines()
    i = 0

    while(i < len(input_data)):
        velocity, time = map(int, input_data[i].split())
        i += 1

        final_v = velocity * 2 * time

        print(final_v)
    
physics()
