# 3040-christmasTree.py
# Problem: The Christmas Tree
# Link: https://judge.beecrowd.com/en/problems/view/3040
# Solved on: 2024-10-17

def christmasTree():
        trees = int(input())
        for _ in range(trees):
            height, diameter, branches = map(int, input().split())
            if height >= 200 and height <=300 and diameter >= 50 and branches >= 150:
                  print('Sim')
            else:
                  print('Nao')

christmasTree()
