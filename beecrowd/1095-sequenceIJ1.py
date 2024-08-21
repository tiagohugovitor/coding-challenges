# 1095-sequenceIJ1.py
# Problem: Sequence IJ 1
# Link: https://judge.beecrowd.com/en/problems/view/1095
# Solved on: 2024-08-20

def sequenceIJ1():
    i = 1
    j = 60

    while j >= 0:
        print(f'I={i} J={j}')
        j -=5
        i += 3

sequenceIJ1()