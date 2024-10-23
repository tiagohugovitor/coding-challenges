# 3145-anUnexpectedJourney.py
# Problem: An unexpected Journey
# Link: https://judge.beecrowd.com/en/problems/view/3145
# Solved on: 2024-10-22

def anUnexpectedJourney():
    dwarves, distance = map(int, input().split())
    time = distance / (dwarves + 2)

    print(f'{time:.2f}')

anUnexpectedJourney()
