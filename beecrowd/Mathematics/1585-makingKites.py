# 1585-makingKites.py
# Problem: Making Kites
# Link: https://judge.beecrowd.com/en/problems/view/1585
# Solved on: 2024-11-19

def makingKites():
    tests = int(input())
    
    for _ in range(tests):    
        width, height = map(int, input().split())
        
        area = (width * height / 2)
        
        print(f'{int(area)} cm2')

makingKites()
