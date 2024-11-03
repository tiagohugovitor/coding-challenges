# 1241-fitOrDontFit.py
# Problem: Fit or Dont Fit II
# Link: https://judge.beecrowd.com/en/problems/view/1241
# Solved on: 2024-11-03

def fitOrDontFit():
    tests = int(input())

    for _ in range(tests):
        greatNumber, lastDigits = input().split()
        
        if len(greatNumber) < len(lastDigits):
            print('nao encaixa')
            continue
        
        endOfGreatNumber = greatNumber[-len(lastDigits):]

        if endOfGreatNumber == lastDigits:
            print('encaixa')
        else:
            print('nao encaixa')

fitOrDontFit()