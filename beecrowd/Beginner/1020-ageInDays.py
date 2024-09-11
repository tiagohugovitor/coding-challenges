# 1019-ageInDays.py
# Problem: Age in Days
# Link: https://judge.beecrowd.com/en/problems/view/1020
# Solved on: 2024-08-18

def ageInDays():
    totalDays = int(input())
    years = totalDays // 365
    totalDays = totalDays % 365
    months = totalDays // 30
    days = totalDays % 30

    print(f'{years} ano(s)')
    print(f'{months} mes(es)')
    print(f'{days} dia(s)')

ageInDays()