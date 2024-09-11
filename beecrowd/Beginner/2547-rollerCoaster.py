# 2547-rollerCoaster.py
# Problem: Roller Coaster
# Link: https://judge.beecrowd.com/en/problems/view/2547
# Solved on: 2024-09-05

def rollerCoaster():
    while True:
        try:
            guests, minHeight, maxHeight = map(int, input().split())
            allowed = 0
            for _ in range(guests):
                height = int(input())
                if minHeight <= height <= maxHeight:
                    allowed += 1

            print(allowed)

        except EOFError:
            break

rollerCoaster()
