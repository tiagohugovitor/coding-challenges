# 2533-internship.py
# Problem: Internship
# Link: https://judge.beecrowd.com/en/problems/view/2533
# Solved on: 2024-09-04

def internship():
    while True:
        try:
            subjects = int(input())
            sumN = 0
            sumC = 0
            for _ in range(subjects):
                n, c = map(int, input().split())
                sumN += (n * c)
                sumC += c
            result = sumN / (sumC * 100)
            print(f'{result:.4f}')

        except EOFError:
            break

internship()
