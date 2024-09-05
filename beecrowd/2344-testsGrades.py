# 2344-testGrades.py
# Problem: Test Grades
# Link: https://judge.beecrowd.com/en/problems/view/2344
# Solved on: 2024-09-04

def testGrades():
    grade = int(input())
    concepts = {
        0: 'E',
        35: 'D',
        60: 'C',
        85: 'B',
        100: 'A',
    }
    for concept in concepts:
        if grade <= concept:
            print(concepts[concept])
            break

testGrades()
