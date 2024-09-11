# 1113-ascendingAndDescending.py
# Problem: Ascending and Descending
# Link: https://judge.beecrowd.com/en/problems/view/1113
# Solved on: 2024-08-21

def ascendingAndDescending():
    x, y = map(int, input().split())
    while x != y:
        if x > y:
            print('Decrescente')
        else:
            print('Crescente')
        x, y = map(int, input().split())

ascendingAndDescending()
