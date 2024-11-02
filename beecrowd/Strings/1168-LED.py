# 1168-LED.py
# Problem: LED
# Link: https://judge.beecrowd.com/en/problems/view/1168
# Solved on: 2024-11-01

def LED():
    ledsAmount = {
        '1': 2,
        '2': 5,
        '3': 5,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 3,
        '8': 7,
        '9': 6,
        '0': 6,
    }

    tests = int(input())

    for _ in range(tests):
        numbers = input()
        totalLeds = 0
        for char in numbers:
            totalLeds += ledsAmount[char]
        
        print(f'{totalLeds} leds')

LED()