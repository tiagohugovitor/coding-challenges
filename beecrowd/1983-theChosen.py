# 1983-theChosen.py
# Problem: The Chosen
# Link: https://judge.beecrowd.com/en/problems/view/1983
# Solved on: 2024-08-28

def theChosen():
    students = int(input())
    biggestGrade = (0, -1)
    for _ in range(students):
        student = input().split()
        id = int(student[0])
        grade = float(student[1])
        if grade > biggestGrade[1]:
            biggestGrade = (id, grade)
    if biggestGrade[1] < 8:
        print('Minimum note not reached')
    else:
        print(biggestGrade[0])

theChosen()
