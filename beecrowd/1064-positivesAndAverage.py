# 1064-positivesAndAverage.py
# Problem: Positive and Average
# Link: https://judge.beecrowd.com/en/problems/view/1064
# Solved on: 2024-08-19

def positivesAndAverage():
    count = 0
    sum = 0
    for _ in range(0, 6):
        value = float(input())
        if value > 0:
            count += 1
            sum += value

    average = sum / count

    print(f'{count} valores positivos')
    print(f'{average:.1f}')

positivesAndAverage()