# 2950-rings2.py
# Problem: The Two Towers
# Link: https://judge.beecrowd.com/en/problems/view/2950
# Solved on: 2024-10-16

def rings2():
    distance, diameter1, diameter2 = map(int, input().split())
    icm = distance / (diameter2 + diameter1)

    print(f'{icm:.2f}')

rings2()
