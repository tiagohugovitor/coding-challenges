# 1768-christmasTree.py
# Problem: Christmas Tree
# Link: https://judge.beecrowd.com/en/problems/view/1768
# Solved on: 2024-11-12

import sys

def christmasTree():
    inputData = sys.stdin.read().strip().splitlines()
    index = 0

    while index < len(inputData):
        size = int(inputData[index])
        index += 1

        start = size // 2
        tree = 1

        while tree <= size:
            for _ in range(start):
                print(' ', end='')
            
            for _ in range(tree):
                print('*', end='')

            print()
            start -= 1
            tree += 2

        start = size // 2

        for _ in range(start):
            print(' ', end='')
        
        print('*')

        start -= 1

        for _ in range(start):
            print(' ', end='')
        
        print('***')

        print()

christmasTree()