# 1096-sequenceIJ2.py
# Problem: Sequence IJ 2
# Link: https://judge.beecrowd.com/en/problems/view/1096
# Solved on: 2024-08-20

def sequenceIJ2():
    i = 1

    while i < 10:
        for j in range(7, 4, -1):
            print(f'I={i} J={j}')
        i += 2

sequenceIJ2()