# 1006-average2.py
# Problem: Average 2
# Link: https://judge.beecrowd.com/en/problems/view/1006
# Solved on: 2024-08-18

def average2():
    a = float(input())
    b = float(input())
    c = float(input())
    average = ((a * 2) + (b * 3) + (c * 5)) / 10
    print(f'MEDIA = {average:.1f}')

average2()