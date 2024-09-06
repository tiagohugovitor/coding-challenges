# 2581-toorg.py
# Problem: I am Toorg!
# Link: https://judge.beecrowd.com/en/problems/view/2581
# Solved on: 2024-09-05

def toorg():
    while True:
        try:
            tests = int(input())
            for _ in range(tests):
                _ = input()
                print('I am Toorg!')

        except EOFError:
            break

toorg()
