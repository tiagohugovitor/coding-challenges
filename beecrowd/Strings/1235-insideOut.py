# 1235-insideOut.py
# Problem: Inside Out
# Link: https://judge.beecrowd.com/en/problems/view/1235
# Solved on: 2024-11-03

def insideOut():
    tests = int(input())

    for _ in range(tests):
        line = input()

        middle = len(line) // 2

        firstHalf = line[middle - 1::-1]
        secondHalf = line[len(line):middle - 1:-1]

        print(f'{firstHalf}{secondHalf}')

insideOut()