# 2062-ObiUri.py
# Problem: OBI URI
# Link: https://judge.beecrowd.com/en/problems/view/2062
# Solved on: 2024-11-12


def ObiUri():
    tests = int(input())

    for _ in range(tests):
        start, end = map(int, input().split())

        ordered = ''

        for number in range(start, end + 1):
            ordered += str(number)

        reversed = ordered[::-1]

        mirror = ordered + reversed

        print(mirror)

ObiUri()