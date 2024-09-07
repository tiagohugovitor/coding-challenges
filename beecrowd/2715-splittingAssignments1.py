# 2715-splittingAssignments1.py
# Problem: Splitting Assignments I
# Link: https://judge.beecrowd.com/en/problems/view/2715
# Solved on: 2024-09-06

def splittingAssignments1():
    while True:
        try:
            n = int(input())
            tasks = list(map(int, input().split()))
            i = 1
            rangel = tasks[0]
            j = n - 1
            gugu = 0

            while j >= i:
                if gugu <= rangel:
                    gugu += tasks[j]
                    j -= 1
                else:
                    rangel += tasks[i]
                    i += 1
            
            print(abs(rangel-gugu))

        except EOFError:
            break

splittingAssignments1()
