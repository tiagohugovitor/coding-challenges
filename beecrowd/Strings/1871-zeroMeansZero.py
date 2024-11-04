# 1871-zeroMeansZero.py
# Problem: Zero means Zero
# Link: https://judge.beecrowd.com/en/problems/view/1871
# Solved on: 2024-11-03

def zeroMeansZero():
    while True:
        numberA, numberB = map(int, input().split())
        
        if numberA == 0 and numberB == 0:
            break
            
        total = str(numberA + numberB)

        filteredTotal = ''.join([char for char in total if char != '0'])

        print(filteredTotal) 

zeroMeansZero()