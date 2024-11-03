# 1272-hiddenMessage.py
# Problem: Hidden Message
# Link: https://judge.beecrowd.com/en/problems/view/1272
# Solved on: 2024-11-03

def hiddenMessage():
    tests = int(input())

    for _ in range(tests):
        foundSpace = True
        line = input()
        hidden = ''

        for char in line:
            if char == ' ':
                foundSpace = True
                continue
            if foundSpace:
                hidden += char
                foundSpace = False

        print(hidden)

hiddenMessage()