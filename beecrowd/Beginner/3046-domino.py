# 3046-domino.py
# Problem: Domino
# Link: https://judge.beecrowd.com/en/problems/view/3046
# Solved on: 2024-10-21

def domino():
    n = int(input())
    result = ((n+1)* (n+2))/ 2

    print(int(result))

domino()
