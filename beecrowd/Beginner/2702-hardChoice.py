# 2702-hardChoice.py
# Problem: Hard Choice
# Link: https://judge.beecrowd.com/en/problems/view/2702
# Solved on: 2024-09-06

def hardChoice():
    available = list(map(int, input().split()))
    orders = list(map(int, input().split()))

    passengersNotReceiving = 0
    for i in range(3):
        if orders[i] > available[i]:
            passengersNotReceiving += (orders[i] - available[i])

    print(passengersNotReceiving)

hardChoice()
