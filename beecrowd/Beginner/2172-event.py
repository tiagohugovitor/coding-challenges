# 2172-event.py
# Problem: Event
# Link: https://judge.beecrowd.com/en/problems/view/2172
# Solved on: 2024-09-02

def event():
    while True:
        amount, xp = map(int, input().split())
        if amount == 0 and xp == 0:
            break
        print(amount*xp)

event()