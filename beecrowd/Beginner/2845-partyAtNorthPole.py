# 2845-partyAtNorthPole.py
# Problem: Party at the North Pole
# Link: https://judge.beecrowd.com/en/problems/view/2845
# Solved on: 2024-10-21

def partyAtNorthPole():
    _ = int(input())
    identifiers = list(map(int, input().split()))

    maximumIdentifier = max(identifiers)

    print(maximumIdentifier + 1)

partyAtNorthPole()
