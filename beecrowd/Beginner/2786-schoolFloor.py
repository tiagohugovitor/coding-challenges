# 2786-schoolFloor.py
# Problem: School Floor
# Link: https://judge.beecrowd.com/en/problems/view/2786
# Solved on: 2024-10-15

def schoolFloor():
    width = int(input())
    length = int(input())
    
    fulls = (width * length) + (width - 1) * (length - 1)
    halfies = (width - 1) * 2 + (length - 1) * 2

    print(fulls)
    print(halfies)

schoolFloor()
