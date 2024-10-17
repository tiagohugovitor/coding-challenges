# 2963-buffoon.py
# Problem: Buffoon
# Link: https://judge.beecrowd.com/en/problems/view/2963
# Solved on: 2024-10-16

def buffoon():
    candidates = int(input())
    carlosVotes = int(input())
    biggest = carlosVotes
    for _ in range(candidates - 1):
        votes = int(input())
        if votes > biggest:
            biggest = votes

    result = 'S' if biggest == carlosVotes else 'N'
    print(result)

buffoon()
