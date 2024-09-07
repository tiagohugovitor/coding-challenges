# 2718-christmasLight.py
# Problem: Christmas Light
# Link: https://judge.beecrowd.com/en/problems/view/2718
# Solved on: 2024-09-06

def christmasLight():
    groups = int(input())
    for _ in range(groups):
        bulbs = int(input())
        binary = ''
        while bulbs > 0:
            binary = f'{bulbs % 2}{binary}'
            bulbs //= 2
        
        maxBulbs = 0
        count = 0
        for char in binary:
            if char == '0':
                if count > maxBulbs:
                    maxBulbs = count
                count = 0
            else:
                count += 1

        if count > maxBulbs:
            maxBulbs = count

        print(maxBulbs)

christmasLight()
