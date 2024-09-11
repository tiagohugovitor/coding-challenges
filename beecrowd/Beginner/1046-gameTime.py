# 1046-gameTime.py
# Problem: Game Time
# Link: https://judge.beecrowd.com/en/problems/view/1046
# Solved on: 2024-08-19

def gameTime():

    start, end = map(int, input().split())
    time = end - start if end > start else 24 - start + end
    print(f'O JOGO DUROU {time} HORA(S)')

gameTime()