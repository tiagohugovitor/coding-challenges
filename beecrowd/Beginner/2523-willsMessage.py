# 2523-willsMessage.py
# Problem: Will's Message
# Link: https://judge.beecrowd.com/en/problems/view/2523
# Solved on: 2024-09-04

def willsMessage():
    while True:
        try:
            alphabet = list(input())
            _ = int(input())
            message = list(map(int, input().split()))

            deciphered = ''.join(list(alphabet[number-1] for number in message))
            print(deciphered)
        except EOFError:
            break

willsMessage()
