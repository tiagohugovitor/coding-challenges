# 1914-whoseTurnIsIt.py
# Problem: Whose Turn Is It?
# Link: https://judge.beecrowd.com/en/problems/view/1914
# Solved on: 2024-08-27

def whoseTurnIsIt():
    tests = int(input())
    for _ in range(tests):
        turn = input().split()
        number1, number2 = map(int, input().split())
        winner = 'PAR' if (number1 + number2) % 2 == 0 else 'IMPAR'
        if winner == turn[1]:
            print(turn[0])
        else:
            print(turn[2])
whoseTurnIsIt()
