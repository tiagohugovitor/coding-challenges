# 1198-hashmat.py
# Problem: Hashmat the Brave Warrior
# Link: https://judge.beecrowd.com/en/problems/view/1198
# Solved on: 2024-11-18

import sys

def hashmat():
    input_data = sys.stdin.read().splitlines()
    i = 0

    while(i < len(input_data)):
        enemySoldiers, hashmatSoldiers = map(int, input_data[i].split())
        i += 1

        print(abs(hashmatSoldiers - enemySoldiers))
    
hashmat()
