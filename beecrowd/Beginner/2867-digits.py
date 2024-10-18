# 2867-digits.py
# Problem: Digits
# Link: https://judge.beecrowd.com/en/problems/view/2867
# Solved on: 2024-10-17

def digits():
    tests = int(input())

    for _ in range(tests):
        n, m = map(int, input().split())
        result = str(pow(n, m))

        print(len(result))


digits()
