# 1013-greatest.py
# Problem: The Greatest
# Link: https://judge.beecrowd.com/en/problems/view/1013
# Solved on: 2024-08-18

def greatest():
    a, b, c = map(int, input().split())

    greaterAB = (a+b+abs(a-b))//2
    greater = (greaterAB+c+abs(greaterAB-c))//2
    print(f'{greater} eh o maior')

greatest()