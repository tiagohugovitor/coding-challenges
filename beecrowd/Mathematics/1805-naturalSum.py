# 1805-naturalSum.py
# Problem: Natural Sum
# Link: https://judge.beecrowd.com/en/problems/view/1805
# Solved on: 2024-11-18

def naturalSum():
    lower, upper = map(int, input().split())

    sum = (lower + upper) * (upper - lower + 1) / 2

    print(int(sum))

naturalSum()
