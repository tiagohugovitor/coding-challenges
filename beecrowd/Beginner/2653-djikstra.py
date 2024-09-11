# 2653-djikstra.py
# Problem: Djikstra
# Link: https://judge.beecrowd.com/en/problems/view/2653
# Solved on: 2024-09-06

def djikstra():
    jewels = set()
    while True:
        try:
            new = input()
            jewels.add(new)

        except EOFError:
            print(len(jewels))
            break

djikstra()
