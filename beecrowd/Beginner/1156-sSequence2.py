# 1156-sSequence2.py
# Problem: S Sequence II
# Link: https://judge.beecrowd.com/en/problems/view/1156
# Solved on: 2024-08-22

def sSequence2():
    sum = 0
    denominator = 1
    for i in range(1, 40, 2):
        sum += (i/denominator)
        denominator *= 2

    print(f'{sum:.2f}') 

sSequence2()