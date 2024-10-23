# 3076-historyExercise.py
# Problem: History Exercise
# Link: https://judge.beecrowd.com/en/problems/view/3076
# Solved on: 2024-10-23

def historyExercise():
    while True:
        try:
            year = int(input())
            century = year // 100

            if year % 100 != 0:
                century += 1
            
            print(century)
        except EOFError:
            break

historyExercise()