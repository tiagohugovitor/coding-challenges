# 1155-sSequence.py
# Problem: S Sequence
# Link: https://judge.beecrowd.com/en/problems/view/1155
# Solved on: 2024-08-22

def sSequence():
    sum = 0
    for i in range(1, 101):
        sum += (1/i)

    print(f'{sum:.2f}') 

sSequence()