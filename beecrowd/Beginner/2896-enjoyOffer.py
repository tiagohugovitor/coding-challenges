# 2896-enjoyOffer.py
# Problem: Enjoy the Offer
# Link: https://judge.beecrowd.com/en/problems/view/2896
# Solved on: 2024-10-17

def enjoyOffer():
    tests = int(input())

    for _ in range(tests):
        bottlesBought, bottleNeeded = map(int, input().split())
        gains = int(bottlesBought / bottleNeeded) + (bottlesBought % bottleNeeded)
        print(gains)


enjoyOffer()
