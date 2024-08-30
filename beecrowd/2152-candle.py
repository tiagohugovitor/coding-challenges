# 2152-candle.py
# Problem: Pepe, I already took the candle!
# Link: https://judge.beecrowd.com/en/problems/view/2152
# Solved on: 2024-08-29

def candle():
    tests = int(input())
    for _ in range(tests):
        hour, minutes, door = map(int, input().split())
        doorAction = 'abriu' if door == 1 else 'fechou'

        print(f'{hour:02}:{minutes:02} - A porta {doorAction}!')
candle()
