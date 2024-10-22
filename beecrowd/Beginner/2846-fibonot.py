# 2846-fibonot.py
# Problem: Fibonot
# Link: https://judge.beecrowd.com/en/problems/view/2846
# Solved on: 2024-10-21

def fibonot():
    index = int(input())
    count = 0
    notFibonnaci = 1

    fibonnaci = [1, 1, 2, 3, 5]

    while count < index:
        if notFibonnaci > fibonnaci[len(fibonnaci) - 1]:
            fibonnaci.append(fibonnaci[len(fibonnaci) - 1] + fibonnaci[len(fibonnaci) - 2])
        if notFibonnaci not in fibonnaci:
            count += 1
        notFibonnaci += 1
    print(notFibonnaci - 1)

fibonot()
