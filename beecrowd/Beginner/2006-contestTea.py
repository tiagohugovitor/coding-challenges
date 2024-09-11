# 2006-contestTea.py
# Problem: Identifying Tea
# Link: https://judge.beecrowd.com/en/problems/view/2006
# Solved on: 2024-08-28

def contestTea():
    correctAnswer = int(input())
    guesses = list(map(int, input().split()))
    correct = 0
    for guess in guesses:
        if guess == correctAnswer:
            correct += 1

    print(correct)

contestTea()
