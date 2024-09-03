# 3348-gameOfSpiders.py
# Problem: Walking on Time
# Link: https://judge.beecrowd.com/en/problems/view/3348
# Solved on: 2024-09-03

# Time Limit Exceed

def gameOfSpiders():
    n = int(input())
    q = n + 1
    while True:
        s, c = [1]*n+[0]*n, 0
        for i in range(n):
            c = (c+q)%(2*n-i)
            if s[c]: break
            s = s[:c]+s[c+1:]
        else:
            print(q+1)
            break
        q += 1

gameOfSpiders()