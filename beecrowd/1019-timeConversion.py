# 1019-timeConversion.py
# Problem: Time Conversion
# Link: https://judge.beecrowd.com/en/problems/view/1019
# Solved on: 2024-08-18

def timeConversion():
    totalDuration = int(input())
    hours = totalDuration // 3600
    totalDuration = totalDuration % 3600
    minutes = totalDuration // 60
    seconds = totalDuration % 60

    print(f'{hours}:{minutes}:{seconds}')

timeConversion()