# 1080-highestAndPosition.py
# Problem: Highest and Position
# Link: https://judge.beecrowd.com/en/problems/view/1080
# Solved on: 2024-08-20

def highestAndPosition():
    max = 0
    position = 0
    
    for i in range(0, 100):
        value = int(input())
        if value > max:
            max = value
            position = i + 1

    print(f'{max}')
    print(f'{position}')

highestAndPosition()