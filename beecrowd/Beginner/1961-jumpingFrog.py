# 1961-jumpingFrog.py
# Problem: Jumping Frog
# Link: https://judge.beecrowd.com/en/problems/view/1961
# Solved on: 2024-08-27

def jumpingFrog():
    jump, pipes = map(int, input().split())
    heihgts = list(map(int, input().split()))
    current = heihgts[0]

    for i in range(1, pipes):
        if abs(heihgts[i] - current) > jump:
            print('GAME OVER')
            return
        current = heihgts[i]

    print('YOU WIN') 

jumpingFrog()
