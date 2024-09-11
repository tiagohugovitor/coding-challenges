# 2717-elfTime.py
# Problem: Elf Time
# Link: https://judge.beecrowd.com/en/problems/view/2717
# Solved on: 2024-09-06

def elfTime():
    remainingTime = int(input())
    giftsTime = list(map(int, input().split()))
    if remainingTime >= giftsTime[0] + giftsTime[1]:
        print('Farei hoje!')
    else:
        print('Deixa para amanha!')

elfTime()
