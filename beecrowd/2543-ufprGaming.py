# 2543-ufprGaming.py
# Problem: UFPR Gaming
# Link: https://judge.beecrowd.com/en/problems/view/2543
# Solved on: 2024-09-05

def ufprGaming():
    while True:
        try:
            n, id = map(int, input().split())
            total = 0
            for video in range(n):
                player, game = map(int, input().split())
                if player == id and game == 0:
                    total += 1
            
            print(total)

        except EOFError:
            break

ufprGaming()
