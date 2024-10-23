# 3084-oldClock.py
# Problem: Old Clock
# Link: https://judge.beecrowd.com/en/problems/view/3084
# Solved on: 2024-10-23

def oldClock():
    while True:
        try:
            hourAngle, minuteAngle = map(int, input().split())
            
            hourNumber = hourAngle // 30
            minuteNumber = minuteAngle // 6

            print(f'{hourNumber:>02}:{minuteNumber:>02}')
        
        except EOFError:
            break

oldClock()