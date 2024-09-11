# 1097-sequenceIJ3.py
# Problem: Sequence IJ 3
# Link: https://judge.beecrowd.com/en/problems/view/1097
# Solved on: 2024-08-20

def sequenceIJ3():
    i = 1
    j = 7
    while i < 10:
        start = j
        for _ in range(0,3):
            print(f'I={i} J={j}')
            j -= 1
        i += 2
        j = start + 2

sequenceIJ3()