# 1323-feynman.py
# Problem: Feynman
# Link: https://judge.beecrowd.com/en/problems/view/1323
# Solved on: 2024-11-18

def chess():
    while True:
        size = int(input())
        
        if size == 0:
            break
        
        squares = 0
        
        while size > 0:
            squares += size * size
            size -= 1
        
        print(squares)

chess()
