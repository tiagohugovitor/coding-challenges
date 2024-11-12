# 1262-multipleReading.py
# Problem: Multiple Reading
# Link: https://judge.beecrowd.com/en/problems/view/1262
# Solved on: 2024-11-12

def multipleReading():
    while True:
        try:
            operations = input()
            procs = int(input())
            clockTimes = 0
            reading = 0
            for operation in operations:
                if reading == procs:
                    reading = 0
                    clockTimes += 1
                
                if operation == 'W':
                    if reading != 0:
                        reading = 0
                        clockTimes += 1
                    clockTimes += 1
                    continue
                
                reading += 1
            
            if reading > 0:
                clockTimes += 1
            
            print(clockTimes)

        except EOFError:
            break

multipleReading()