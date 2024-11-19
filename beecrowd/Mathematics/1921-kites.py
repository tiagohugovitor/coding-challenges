# 1921-kites.py
# Problem: Guilherme and His Kites
# Link: https://judge.beecrowd.com/en/problems/view/1921
# Solved on: 2024-11-19

def kites():
    
    size = int(input())
    
    strings = size * (size - 3) / 2
    
    print(int(strings))

kites()
