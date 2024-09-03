# 2234-hotDogs.py
# Problem: Hot Dogs
# Link: https://judge.beecrowd.com/en/problems/view/2234
# Solved on: 2024-09-02

def hotDogs():
    consumed, people = map(int, input().split())

    average = consumed / people

    print(f'{average:.2f}')

hotDogs()
