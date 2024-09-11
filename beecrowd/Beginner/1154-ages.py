# 1154-ages.py
# Problem: Ages
# Link: https://judge.beecrowd.com/en/problems/view/1154
# Solved on: 2024-08-22

def ages():
    n = int(input())
    sum = 0
    total = 0
    while n >= 0:
        sum += n 
        total += 1
        n = int(input())
    average = 0 if total == 0 else sum/total
    print(f'{average:.2f}') 

ages()