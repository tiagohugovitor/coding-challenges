# 1930-electricalOutlet.py
# Problem: Electrical Outlet
# Link: https://judge.beecrowd.com/en/problems/view/1930
# Solved on: 2024-08-27

def electricalOutlet():
    a, b, c, d = map(int, input().split())
    print(a + b + c + d - 3)
    
electricalOutlet()
