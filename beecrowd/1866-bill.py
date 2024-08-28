# 1866-bill.py
# Problem: Bill
# Link: https://judge.beecrowd.com/en/problems/view/1866
# Solved on: 2024-08-27

def bill():
    tests = int(input())
    for _ in range(tests):
        numberOfTerms = int(input())
        if numberOfTerms % 2 == 0:
            print('0')
        else:
            print('1')

bill()
