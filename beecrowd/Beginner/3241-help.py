# 3241-help.py
# Problem: Help a PhD Candidate Out!
# Link: https://judge.beecrowd.com/en/problems/view/3241
# Solved on: 2024-10-30

def help():
    tests = int(input())

    for _ in range(tests):
        operation = input()
        
        if operation == 'P=NP':
            print('skipped')
            continue

        firstOperator, secondOperator = operation.split('+')
        print(int(firstOperator) + int(secondOperator))

help()
