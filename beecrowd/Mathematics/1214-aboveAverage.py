# 1214-aboveAverage.py
# Problem: Above Average
# Link: https://judge.beecrowd.com/en/problems/view/1214
# Solved on: 2024-11-18

def aboveAverage():
    tests = int(input())

    for _ in range(tests):
        grades = list(map(int, input().split()))
        average = 0

        for student in range(grades[0]):
            average += grades[student + 1]
        
        average /= grades[0]
        
        studentsAboveAverage = 0

        for student in range(grades[0]):
            if grades[student + 1] > average:
                studentsAboveAverage += 1

        print(f'{studentsAboveAverage * 100 / grades[0]:.3f}%')
        


aboveAverage()
