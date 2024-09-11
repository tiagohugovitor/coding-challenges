# 1847-welcomeToTheWinter.py
# Problem: Welcome to the Winter!
# Link: https://judge.beecrowd.com/en/problems/view/1847
# Solved on: 2024-08-26

def welcomeToTheWinter():
    days = list(map(int, input().split()))

    if ((days[0] > days[1] and days[1] <= days[2]) or
        (days[0] < days[1] and days[1] < days[2] and (days[2] - days[1] >= days[1] - days[0])) or
        (days[0] > days[1] and days[1] > days[2] and (days[0] - days[1] > days[1] - days[2])) or
        (days[0] == days[1] and days[1] < days[2])):
        print(':)')
    else:
        print(':(')

welcomeToTheWinter()
