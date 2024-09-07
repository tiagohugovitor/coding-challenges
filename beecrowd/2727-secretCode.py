# 2727-secretCode.py
# Problem: Indecision of Reindeers
# Link: https://judge.beecrowd.com/en/problems/view/2727
# Solved on: 2024-09-06

def secretCode():
    while True:
        try:
            tests = int(input())
            for _ in range(tests):
                word = list(input().split())
                size = (len(word) - 1) * 3 + len(word[0]) - 1
                print(chr(ord('a') + size))
                
        except EOFError:
            break

secretCode()
