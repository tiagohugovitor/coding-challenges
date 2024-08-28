# 1933-triDu.py
# Problem: Tri-du
# Link: https://judge.beecrowd.com/en/problems/view/1933
# Solved on: 2024-08-27

def triDu():
    a, b = map(int, input().split())
    if a >= b:
        print(a)
    else:
        print(b)
    
triDu()
